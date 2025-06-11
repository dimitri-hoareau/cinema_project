from rest_framework import viewsets,  mixins, status
from rest_framework.response import Response
from core.models import Author
from .serializers import AuthorSerializer

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

