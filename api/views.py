from rest_framework import viewsets,  mixins, status
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