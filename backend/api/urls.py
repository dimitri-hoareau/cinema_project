from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, FilmViewSet, SpectatorRegistrationView, LogoutView, FavoriteMoviesListView, MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView



router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'films', FilmViewSet, basename='film')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/register/', SpectatorRegistrationView.as_view(), name='spectator-register'),
    path('auth/logout/', LogoutView.as_view(), name='auth_logout'),
    path('spectator/favorites/', FavoriteMoviesListView.as_view(), name='list-favorite-movies'),
]