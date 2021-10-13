from django.shortcuts import redirect, render
from django.urls import reverse
from rest_framework import response, status, decorators

from .models import Music,Artist, Playlist
from .serializers import MusicSerializer


@decorators.api_view(['GET'])
def json_view(request, id):
    artist=Artist.objects.get(id=id)
    musics = artist.music_set.all()
    serializer = MusicSerializer(musics, many=True)
    return response.Response(serializer.data, status=status.HTTP_200_OK)

@decorators.api_view(['GET'])
def searchjson_view(request):
    # artist=Artist.objects.get(id=id)
    musics = Music.objects.all()
    serializer = MusicSerializer(musics, many=True)
    return response.Response(serializer.data, status=status.HTTP_200_OK)


def home(request):
    artistid = request.GET.get('artist')
    songid=request.GET.get('song')
    print(songid)
    context = {}
    if songid:
        # song=Music.objects.get(id=int(songid))
        context["song"] = songid
    if artistid:
        artist=Artist.objects.get(id=int(artistid))
        context["artist"] = artist
    return render(request, 'app/index.html', context)


def artist_view(request):
    artist=Artist.objects.all()
    context={
        'artist':artist
    }
    return render(request,'app/artist.html',context)

def songs_view(request,id):
    user = request.user
    if not user.is_authenticated:
        return redirect(reverse('loginform'))

    artist=Artist.objects.get(id=id)
    playlist = Playlist.objects.filter(user=user)
    context={
        'a':artist,
        "playlistsongs": playlist[0].songs.all()
    }
    return render(request,'app/songs.html',context)

def search_view(request):
    musics = Music.objects.all()

    search_term = request.GET.get('search')
    if search_term:
        musics=musics.filter(name__icontains=search_term)
    context={
        'songs':musics
    }
    return render(request,'app/search.html',context)