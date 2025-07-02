from rest_framework import viewsets,  mixins, status,generics, permissions
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.views import TokenObtainPairView
from core.models import Author, Film, User, FilmRating, AuthorRating, Spectator
from .serializers import AuthorSerializer, FilmSerializer, SpectatorRegistrationSerializer, RatingSerializer,MyTokenObtainPairSerializer
class AuthorViewSet(mixins.ListModelMixin,       
                    mixins.RetrieveModelMixin,    
                    mixins.UpdateModelMixin,      
                    mixins.DestroyModelMixin,    
                    viewsets.GenericViewSet): 
    """
    ViewSet for CRUD operation on author.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    serializer_class = AuthorSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned authors,
        by filtering against a source parameter in the URL.
        """
        queryset = Author.objects.all()
        source = self.request.query_params.get('source')
        if source is not None:
            queryset = queryset.filter(source=source)
        return queryset

    def destroy(self, request, *args, **kwargs):
        author = self.get_object()
        if author.films.count() > 0:
            return Response(
                {'error': "Can't delete an author who have a movie"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().destroy(request, *args, **kwargs)
    

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def rate(self, request, pk=None):
        """
        Allow authenticated user to score a author
        """
        author = self.get_object()

        try:
            spectator = request.user.spectator
        except Spectator.DoesNotExist:
            return Response({'error': 'Only a spectator can rank a author'}, status=status.HTTP_403_FORBIDDEN)

        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            score = serializer.validated_data['score']

            AuthorRating.objects.update_or_create(
                author=author,
                spectator=spectator,
                defaults={'score': score}
            )
            return Response({'status': 'score saved'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class FilmViewSet(mixins.ListModelMixin,       
                    mixins.RetrieveModelMixin,    
                    mixins.UpdateModelMixin,         
                    viewsets.GenericViewSet): 
    """
    ViewSet for CRUD operation on film.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    serializer_class = FilmSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned Films,
        by filtering against a source parameter in the URL.
        """
        queryset = Film.objects.all()
        source = self.request.query_params.get('source')
        if source is not None:
            queryset = queryset.filter(source=source)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        status_filter = request.query_params.get('status', None)

        if status_filter is not None:
            queryset = queryset.filter(status=status_filter)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def archive(self, request, pk=None):
        """
        custom method to archive a movie.
        Change movie status to 'archived'.
        """
        film = self.get_object()
        film.status = 'archived'
        film.save()

        return Response(
            {'status': f"The movie'{film.title}' is correctly archived."},
            status=status.HTTP_200_OK
        )
    
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def rate(self, request, pk=None):
        """
        Allow authenticated user to score a movie
        """
        film = self.get_object()

        try:
            spectator = request.user.spectator
        except Spectator.DoesNotExist:
            return Response({'error': 'Only a spectator can rank a movie'}, status=status.HTTP_403_FORBIDDEN)

        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            score = serializer.validated_data['score']

            FilmRating.objects.update_or_create(
                film=film,
                spectator=spectator,
                defaults={'score': score}
            )
            return Response({'status': 'score saved'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def add_favorite(self, request, pk=None):
        """
        Allow spectator to add movie to his favorite
        """
        film = self.get_object() 
        
        try:
            spectator = request.user.spectator
        except Spectator.DoesNotExist:
            return Response({'error': 'Only a spectator can have favorite.'}, status=status.HTTP_403_FORBIDDEN)

        spectator.favorite_movies.add(film)
        
        return Response(
            {'status': f"Movie '{film.title}' added to favorites."},
            status=status.HTTP_200_OK
        )
    
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def remove_favorite(self, request, pk=None):
        """
        Allow spectator to remove movie to his favorite
        """
        film = self.get_object() 
        
        try:
            spectator = request.user.spectator
        except Spectator.DoesNotExist:
            return Response({'error': 'Only a spectator can have favorite.'}, status=status.HTTP_403_FORBIDDEN)

        spectator.favorite_movies.remove(film)
        
        return Response(
            {'status': f"Movie '{film.title}' removed from favorites."},
            status=status.HTTP_200_OK
        )


class SpectatorRegistrationView(generics.CreateAPIView):
    """
    Endpoint for creating a new Spectator.
    """
    queryset = User.objects.all()
    serializer_class = SpectatorRegistrationSerializer
    permission_classes = [permissions.AllowAny]

class LogoutView(APIView):
    """
    View for user logout.
    Add refresh token to blacklist.
    """
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

class FavoriteMoviesListView(generics.ListAPIView):
    """
    List favorite movie from on user
    """
    serializer_class = FilmSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        return only favorite movie and not all the Films queryset
        """
        user = self.request.user
        
        try:
            spectator = user.spectator
        except Spectator.DoesNotExist:
            return Film.objects.none()

        return spectator.favorite_movies.all()

class MyTokenObtainPairView(TokenObtainPairView):
    """
    view for the custom token serializer
    """
    serializer_class = MyTokenObtainPairSerializer