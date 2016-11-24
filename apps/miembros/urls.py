from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required as lr
from apps.miembros.views import MemberRegister, ArtistRegister, ArtistEditProfile, NotificarInscripcion, RequestList, DetailRequest

urlpatterns = [
#    url(r'^listArtist$', ArtistList.as_view(), name = 'inicio'),
    url(r'^new_member$', MemberRegister.as_view(), name = 'member_create'),
    url(r'^artist_profile/(?P<pk>\d+)$', lr(ArtistRegister.as_view()), name = 'artist_manage'),
    url(r'^(?P<pk>\d+)$', lr(ArtistEditProfile.as_view()), name = 'artist_edit'),
    url(r'^send_email/$', lr(NotificarInscripcion), name = 'notify_request'),
    url(r'^requests/$', lr(RequestList.as_view()), name = 'requests_list'),
    url(r'^detail/(?P<pk>\d+)$', lr(DetailRequest.as_view()), name = 'request_detail'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
