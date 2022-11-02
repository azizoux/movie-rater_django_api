from django.contrib import admin
from django.utils.html import format_html
from .models import Movie, Rating


class MovieAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" style="border-radius:50px;" width="50" />'.format(object.image))

    thumbnail.short_description = 'Movie Image'

    list_display = ('id', 'thumbnail', 'title', 'nb_of_ratings', 'avg_ratings', 'liked')
    list_display_links = ('id', 'thumbnail', 'title')
    list_editable = ('liked', )
    search_fields = ('id', 'title', 'liked',)


admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating)