from django.conf.urls import url
from app.views import ArtistCreate, home

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^newArtist$', ArtistCreate.as_view(), name = 'artist_create'),
]
