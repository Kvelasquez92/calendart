from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.views.generic import FormView
from django.contrib.auth import authenticate, login
from django.contrib import messages
from apps.miembros.models import Member
from apps.miembros.forms import MemberForm, ArtistForm, ArtistProfileForm
from django.core.mail import EmailMessage
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from django.conf import settings

# Create your views here.

class MemberRegister(FormView):
    model = Member
    form_class = MemberForm
    template_name = 'miembros/member_form.html'
    success_url = reverse_lazy('home:index')

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        messages.add_message(self.request, messages.INFO, 'Gracias por registrarte, ahora estas autenticado!!')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(MemberRegister, self).form_valid(form)

def ArtistRegister1(request, pk):
    miembro = Member.objects.get(id=pk)
    if request.method == 'GET':
        form = ArtistForm(instance=miembro)
    else:
        form = ArtistForm(request.POST, instance=miembro)
        if form.is_valid():
            form.save()
            NotificarInscripcion(request)
            return redirect('home:index')
    return render (request, 'miembros/artist_form.html', {'form': form})

class ArtistRegister(UpdateView):
    model = Member
    form_class = ArtistForm
    template_name = 'miembros/artist_form.html'
    success_url = reverse_lazy('home:index')

def NotificarInscripcion(request):
    superusuarios = Member.objects.filter(is_superuser=True)
    correos = []
    for superusuario in superusuarios:
        correos.append(superusuario.email)
    path = request.POST['image_profile']
    print (path)
    img_data = open(os.path.join(settings.MEDIA_ROOT, path), 'rb').read()
    msg = MIMEMultipart(_subtype='related')
    body = MIMEText('<p>Hello <img src="cid:myimage" /></p>', _subtype='html')
    msg.attach(body)
    img = MIMEImage(img_data, 'jpeg')
    img.add_header('Content-Id', '<myimage>')
    msg.attach(img)
    asunto = 'Nuevas solicitud de inscripción de Artista!'
    mail = EmailMessage(asunto, msg.as_string(), from_email='Cultural <chicle.kevin@gmail.com>', to = correos)
    mail.send()

class ArtistEditProfile(UpdateView):
    model = Member
    form_class = ArtistProfileForm
    template_name = 'miembros/artist_profile_form.html'
    success_url = reverse_lazy('home:index')
