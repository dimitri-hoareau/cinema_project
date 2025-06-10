from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Author, Film, Spectator, AuthorRating, FilmRating

admin.site.register(User, UserAdmin)
admin.site.register(Author)
admin.site.register(Spectator)
admin.site.register(AuthorRating)
admin.site.register(FilmRating)

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_at')
    readonly_fields = ('created_at',)
    list_filter = ( 'status', 'evaluation', 'created_at')
