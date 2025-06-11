from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, FilmViewSet, SpectatorRegistrationView, LogoutView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'films', FilmViewSet, basename='film')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/register/', SpectatorRegistrationView.as_view(), name='spectator-register'),
    path('auth/logout/', LogoutView.as_view(), name='auth_logout'),
]