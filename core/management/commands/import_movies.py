import os
import requests
from datetime import date
from django.core.management.base import BaseCommand
from core.models import Film, Author, StatusChoices, SourceChoices

class Command(BaseCommand):
    help = 'Imports popular movies from The Movie Database (TMDb).'

    def handle(self, *args, **options):
        api_key = os.getenv('TMDB_API_KEY')
        movies_url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&page=1"
        response = requests.get(movies_url)
        movies_data = response.json().get('results', [])

        for movie_data in movies_data:
            print(movie_data)

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
            
            author_obj, _ = Author.objects.get_or_create(
                name=final_author_name,
                defaults={'source': SourceChoices.TMDB}
            )

            # second step, get and create the movie with the related author
            release_date_str = movie_data.get('release_date')
            movie_status = StatusChoices.RELEASED 
            

            release_date_obj = date.fromisoformat(release_date_str)
            if release_date_obj > date.today():
                movie_status = StatusChoices.PROJECT

            movie_obj, created = Film.objects.update_or_create(
                title=movie_data['title'],
                release_date=release_date_str,
                defaults={
                    'description': movie_data.get('overview', ''),
                    'author': author_obj,
                    'status': movie_status,
                    'source': SourceChoices.TMDB
                }
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f"  -> Movie '{movie_obj.title}' imported."))
            else:
                self.stdout.write(f"  -> Movie '{movie_obj.title}' already exists.")
        