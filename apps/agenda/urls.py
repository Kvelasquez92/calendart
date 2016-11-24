from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from apps.agenda.views import Home, Home2, EventCreate, EventList, DetalleEvento

urlpatterns = [
    url(r'^home$', Home, name='index'),
    url(r'^(?P<pk>\d+)$', Home2, name='index2'),
    url(r'^new_event$', EventCreate.as_view(), name = 'event_create'),
    url(r'^list', EventList, name = 'event_list'),
    url(r'^(?P<pk>\d+)$', DetalleEvento.as_view(), name='detalle_evento'),
#    url(r'^updateArtist/(?P<pk>\d+)$', ArtistUpdate.as_view(), name = 'artist_update'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
