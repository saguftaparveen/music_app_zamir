from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static

from music.views import (json_view, home, artist_view,
                         songs_view, search_view, searchjson_view, update_playlist,)

urlpatterns = [
    path('music/', home),
    path('', include('post.urls')),
    path('songs/<int:id>/', json_view),
    path('allsongs/', searchjson_view),
    path('artists/', artist_view),
    path('artists/<int:id>/', songs_view),
    path('search/', search_view),
    path('update_playlist/<int:song_id>/', update_playlist),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
