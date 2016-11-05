from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from apps.agenda.views import home, EventCreate

urlpatterns = [
    url(r'^$', home, name='index'),
    url(r'^new_event$', EventCreate.as_view(), name = 'event_create'),
#    url(r'^new_member$', MemberRegister.as_view(), name = 'member_create'),
#    url(r'^updateArtist/(?P<pk>\d+)$', ArtistUpdate.as_view(), name = 'artist_update'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
