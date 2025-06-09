from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

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
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    source = models.CharField(
        max_length=10,
        choices=SourceChoices.choices,
        default=SourceChoices.ADMIN
    )

    def __str__(self):
        return self.name
