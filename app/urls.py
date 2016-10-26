from django.conf.urls import url
from app.views import ArtistCreate

urlpatterns = [
    url(r'^newArtist$', ArtistCreate.as_view(), name = 'artist_create'),
]
