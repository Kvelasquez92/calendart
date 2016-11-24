from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required as lr
from apps.miembros.views import MemberRegister, ArtistRegister, ArtistEditProfile

urlpatterns = [
#    url(r'^listArtist$', ArtistList.as_view(), name = 'inicio'),
    url(r'^new_member$', MemberRegister.as_view(), name = 'member_create'),
    url(r'^artist_profile/(?P<pk>\d+)$', lr(ArtistRegister.as_view()), name = 'artist_manage'),
    url(r'^(?P<pk>\d+)$', lr(ArtistEditProfile.as_view()), name = 'artist_edit'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
