from rest_framework import viewsets,  mixins, status,generics, permissions
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.decorators import action
from core.models import Author, Film, User
from .serializers import AuthorSerializer, FilmSerializer, SpectatorRegistrationSerializer

class AuthorViewSet(mixins.ListModelMixin,       
                    mixins.RetrieveModelMixin,    
                    mixins.UpdateModelMixin,      
                    mixins.DestroyModelMixin,    
                    viewsets.GenericViewSet): 
    """
    ViewSet for CRUD operation on author.
    """

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def destroy(self, request, *args, **kwargs):
        author = self.get_object()
        if author.films.count() > 0:
            return Response(
                {'error': "Can't delete an author who have a movie"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().destroy(request, *args, **kwargs)

class FilmViewSet(mixins.ListModelMixin,       
                    mixins.RetrieveModelMixin,    
                    mixins.UpdateModelMixin,         
                    viewsets.GenericViewSet): 
    """
    ViewSet for CRUD operation on film.
    """

    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        status_filter = request.query_params.get('status', None)

        if status_filter is not None:
            queryset = queryset.filter(status=status_filter)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
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