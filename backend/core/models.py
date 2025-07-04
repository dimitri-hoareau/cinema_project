from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import AbstractUser
from django.db import models

class EvaluationChoices(models.IntegerChoices):
        ONE = 1, '⭐'
        TWO = 2, '⭐⭐'
        THREE = 3, '⭐⭐⭐'
        FOUR = 4, '⭐⭐⭐⭐'
        FIVE = 5, '⭐⭐⭐⭐⭐'

class StatusChoices(models.TextChoices):
        RELEASED = 'released', 'Released'
        PROJECT = 'project', 'Project'
        ARCHIVED = 'archived', 'Archived'

class SourceChoices(models.TextChoices):
        ADMIN = 'admin', 'Admin' 
        TMDB = 'tmdb', 'TMDb'

class User(AbstractUser):
    """
    Base user model for authentication.
    Inherits from AbstractUser to keep Django's auth system.
    """
    pass

class Author(models.Model):
    """
    Author Profile. Contains author-specific information.
    """

    name = models.CharField(max_length=255, unique=True)
    birth_date = models.DateField(null=True, blank=True)
    source = models.CharField(
        max_length=10,
        choices=SourceChoices.choices,
        default=SourceChoices.ADMIN
    )

    def __str__(self):
        return self.name

class Film(models.Model):
    """
    Film Profile. Contains film-specific information.
    """


    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='films')
    title = models.CharField(max_length=255)
    description = models.TextField()
    # poster_path = models.CharField(max_length=255, null=True, blank=True)
    poster_original = models.ImageField(upload_to='posters/originals/', null=True, blank=True)
    poster_thumbnail = ImageSpecField(source='poster_original',
                                      processors=[ResizeToFill(200, 300)], 
                                      format='JPEG',
                                      options={'quality': 85})
    backdrop_path = models.CharField(max_length=255, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Date de Création"
    )
    evaluation = models.IntegerField(
        choices=EvaluationChoices.choices,
        null=True, blank=True 
    )
    status = models.CharField(
        max_length=10,
        choices=StatusChoices.choices,
    )
    source = models.CharField(
        max_length=10,
        choices=SourceChoices.choices,
        default=SourceChoices.ADMIN
    )

    def __str__(self):
        return self.title
    

class Spectator(models.Model):
    """
    Spectator Profile. Contains spectator-specific information.
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    bio = models.TextField(blank=True) 
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    favorite_movies = models.ManyToManyField('Film', blank=True)

    def __str__(self):
        return self.name
    
    @property
    def name(self):
        return self.user.username

class AuthorRating(models.Model):
    """
    Represents a single rating given by a Spectator to an Author.

    """
    spectator = models.ForeignKey(Spectator, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='ratings')
    score = models.IntegerField(
        choices=EvaluationChoices.choices,
        null=True, blank=True 
    )

    def __str__(self):
        return f"Rank of {self.spectator} for {self.author} : {self.get_score_display()}"

class FilmRating(models.Model):
    """
    Represents a single rating given by a Spectator to an Film.

    """
    spectator = models.ForeignKey(Spectator, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='ratings')
    score = models.IntegerField(
        choices=EvaluationChoices.choices,
        null=True, blank=True 
    )
    def __str__(self):
        return f"Rank of {self.spectator} for {self.film} : {self.get_score_display()}"