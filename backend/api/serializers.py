from rest_framework import serializers
from core.models import Author, Film, User, Spectator, EvaluationChoices
class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for Author model.
    """
    class Meta:
        model = Author
        fields = ['id', 'name', 'birth_date', 'source']

class FilmSerializer(serializers.ModelSerializer):
    """
    Serializer for Film model.
    """
    author = AuthorSerializer()

    class Meta:
        model = Film
        fields = ['id', 'author', 'title', 'description', 'release_date', 'evaluation', 'status']

class SpectatorRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for spectator registration.
    Create User object and linked Spectator
    """
    bio = serializers.CharField(write_only=True, required=False, allow_blank=True)
    avatar = serializers.ImageField(write_only=True, required=False)
    password_confirm = serializers.CharField(style={'input_type': 'password'}, write_only=True)


    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirm', 'bio', 'avatar')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):

        bio_data = validated_data.pop('bio', '')
        avatar_data = validated_data.pop('avatar', None)
        password_confirm_data = validated_data.pop('password_confirm', None)
        user = User.objects.create_user(**validated_data)
        
        Spectator.objects.create(
            user=user,
            bio=bio_data,
            avatar=avatar_data
        )
        return user

class RatingSerializer(serializers.Serializer):
    """
    Validate a choice on defined rank.
    """
    score = serializers.ChoiceField(choices=EvaluationChoices.choices)
