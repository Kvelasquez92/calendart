from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from apps.miembros.views import MemberRegister

urlpatterns = [
#    url(r'^listArtist$', ArtistList.as_view(), name = 'inicio'),
    url(r'^new_member$', MemberRegister.as_view(), name = 'member_create'),
#    url(r'^updateArtist/(?P<pk>\d+)$', ArtistUpdate.as_view(), name = 'artist_update'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
