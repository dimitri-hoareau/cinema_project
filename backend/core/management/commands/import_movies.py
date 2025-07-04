import os
import requests
from datetime import date
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from core.models import Film, Author, StatusChoices, SourceChoices

class Command(BaseCommand):
    help = 'Imports popular movies from The Movie Database (TMDb).'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('--- Commande démarrée ---'))
        api_key = os.getenv('TMDB_API_KEY')
        pages_to_fetch = 5 
        for page_num in range(1, pages_to_fetch + 1):
            movies_url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&page={page_num}"
            response = requests.get(movies_url)
            movies_data = response.json().get('results', [])

            if not movies_data:
                self.stdout.write(self.style.WARNING("No movies found on this page, stopping."))
                break


            for movie_data in movies_data:

                # First step, get and create the author
                movie_id = movie_data['id']
                credits_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}"
                credits_response = requests.get(credits_url)
                crew_list = credits_response.json().get('crew', [])

                director_name = None
                writer_name = None

                for member in crew_list:
                    if member.get('job') == 'Director':
                        director_name = member.get('name')
                        break 
                    elif member.get('job') == 'Writer' and not writer_name:
                        writer_name = member.get('name')

                final_author_name = director_name if director_name else writer_name

                if not final_author_name:
                    self.stdout.write(self.style.WARNING(f"  -> Can't fin any Author for movie ID {movie_id}. Ignored."))
                    continue 
                
                author_obj, _ = Author.objects.get_or_create(
                    name=final_author_name,
                    defaults={'source': SourceChoices.TMDB}
                )

                # second step, get and create the movie with the related author
                release_date_str = movie_data.get('release_date')

                if not release_date_str:
                    self.stdout.write(self.style.WARNING(f"  -> No release date for movie '{movie_data['title']}'. Ignored."))
                    continue

                movie_status = StatusChoices.RELEASED
                release_date_obj = date.fromisoformat(release_date_str)
                if release_date_obj > date.today():
                    movie_status = StatusChoices.PROJECT

                vote_average = movie_data.get('vote_average', 0)
                evaluation_score = int(round(vote_average / 2))

                backdrop_path_segment = movie_data.get('backdrop_path')
                backdrop_url = f"https://image.tmdb.org/t/p/w1280/{backdrop_path_segment}" if backdrop_path_segment else ''

                movie_obj, created = Film.objects.update_or_create(
                    title=movie_data['title'],
                    defaults={
                        'description': movie_data.get('overview', ''),
                        'author': author_obj,
                        'release_date': release_date_obj,
                        'status': movie_status,
                        'source': SourceChoices.TMDB,
                        'evaluation': evaluation_score,
                        'backdrop_path': backdrop_url
                    }
                )

                if created or not movie_obj.poster_original:
                    poster_path_segment = movie_data.get('poster_path')
                    if poster_path_segment:
                        image_url = f"https://image.tmdb.org/t/p/original{poster_path_segment}"
                        
                        try:
                            response = requests.get(image_url, stream=True)
                            response.raise_for_status()  # Lève une erreur en cas de 4xx/5xx

                            file_name = image_url.split("/")[-1]
                            
                            movie_obj.poster_original.save(
                                file_name,
                                ContentFile(response.content),
                                save=True  
                            )
                            self.stdout.write(self.style.SUCCESS(f"  -> Image for '{movie_obj.title}' downloaded and saved."))

                        except requests.exceptions.RequestException as e:
                            self.stdout.write(self.style.WARNING(f"  -> Could not download image for '{movie_obj.title}': {e}"))

                if created:
                    self.stdout.write(self.style.SUCCESS(f"  -> Movie '{movie_obj.title}' imported."))
                else:
                    self.stdout.write(f"  -> Movie '{movie_obj.title}' already exists.")
            