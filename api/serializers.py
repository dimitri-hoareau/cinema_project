from rest_framework import serializers
from core.models import Author, Film

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for Author model.
    """
    class Meta:
        model = Author
        fields = ['user_id', 'name', 'birth_date', 'source']

class FilmSerializer(serializers.ModelSerializer):
    """
    Serializer for Film model.
    """
    author = serializers.StringRelatedField()

    class Meta:
        model = Film
        fields = ['id', 'author', 'title', 'description', 'release_date', 'evaluation', 'status']