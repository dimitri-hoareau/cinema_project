from rest_framework import viewsets,  mixins, status
from rest_framework.response import Response
from rest_framework.decorators import action
from core.models import Author, Film
from .serializers import AuthorSerializer, FilmSerializer

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

