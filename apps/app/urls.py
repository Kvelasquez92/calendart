from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from app.views import ArtistCreate, ArtistList, ArtistUpdate, EventCreate, NoteCreate, home

urlpatterns = [
    url(r'^$', home, name='index'),
    url(r'^listArtist$', ArtistList.as_view(), name = 'inicio'),
    url(r'^newArtist$', ArtistCreate.as_view(), name = 'artist_create'),
    url(r'^updateArtist/(?P<pk>\d+)$', ArtistUpdate.as_view(), name = 'artist_update'),
    url(r'^newEvent$', EventCreate.as_view(), name = 'event_create'),
    url(r'^newNote$', NoteCreate.as_view(), name = 'note_create'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
