from django.contrib import admin

from .models import Music, Artist,Playlist

admin.site.register(Music)
admin.site.register(Playlist)
admin.site.register(Artist)
