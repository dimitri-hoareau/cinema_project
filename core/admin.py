from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db.models import Count
from .models import User, Author, Film, Spectator, AuthorRating, FilmRating

class FilmInline(admin.TabularInline):
    model = Film
    fields = ('title',)
    extra = 0

class RankFilmInline(admin.TabularInline):
    model = FilmRating
    fields = ('spectator','score')
    extra = 0


class AuthorHasFilmFilter(admin.SimpleListFilter):
    title = 'Produced films'
    parameter_name = 'has_films'

    def lookups(self, request, model_admin):
        return [
            ('yes', 'With at least one movie'),
            ('no', 'With no movies'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            annotated_queryset = queryset.annotate(num_films=Count('films'))
            filtered_queryset = annotated_queryset.filter(num_films__gt=0)

            return filtered_queryset
        
        if self.value() == 'no':
            annotated_queryset = queryset.annotate(num_films=Count('films'))
            filtered_queryset = annotated_queryset.filter(num_films__exact=0)

            return filtered_queryset

admin.site.register(User, UserAdmin)
admin.site.register(Spectator)
admin.site.register(AuthorRating)
admin.site.register(FilmRating)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """admin config for Author Model."""
    list_filter = (AuthorHasFilmFilter,)
    inlines = [FilmInline]

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    """admin config for Film Model."""
    readonly_fields = ('created_at',)
    list_filter = ( 'status', 'evaluation', 'created_at')
    inlines = [RankFilmInline]

