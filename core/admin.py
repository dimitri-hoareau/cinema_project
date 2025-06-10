from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Author, Film, Spectator, AuthorRating

admin.site.register(User, UserAdmin)
admin.site.register(Author)
admin.site.register(Film)
admin.site.register(Spectator)
admin.site.register(AuthorRating)