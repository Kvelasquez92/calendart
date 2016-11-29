from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, UpdateView, FormView, ListView, DetailView
from django.contrib.auth import authenticate, login
from django.contrib import messages
from apps.miembros.models import Member
from apps.miembros.forms import MemberForm, ArtistForm, ArtistProfileForm
from django.core.mail import EmailMessage
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
    automensaje = '\t\tEl perfil del usuario ' + request.user.username + 'es:' '\n\n'
    automensaje = automensaje + 'Nombre(s): ' + request.user.first_name + '\n\n'
    automensaje = automensaje + 'Apellidos(s): ' + request.user.last_name + '\n\n'
    automensaje = automensaje + 'Fecha de nacimiento: ' + request.user.date_of_birth.strftime('%d/%m/%Y') + '\n\n'
    automensaje = automensaje + 'Tel: ' + request.user.phone_number + '\n\n'
    automensaje = automensaje + 'Dirección: ' + request.user.address + '\n\n'
    automensaje = automensaje + 'Autobiografía: ' + request.user.biography + '\n\n'
    asunto = 'Nuevas solicitud de inscripción!!'
    mail = EmailMessage(asunto, automensaje, from_email='Cultural <chicle.kevin@gmail.com>', to = correos)
    mail.attach_file(os.path.join(settings.MEDIA_ROOT, request.user.image_profile.path))
    mail.send()
    return redirect('home:index')

class ArtistEditProfile(UpdateView):
    model = Member
    form_class = ArtistProfileForm
    template_name = 'miembros/artist_profile_form.html'
    success_url = reverse_lazy('home:index')

class RequestList(ListView):
    template_name='miembros/requests.html'
    model = Member
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(RequestList, self).get_context_data(**kwargs)
        context['solicitudes'] = Member.objects.filter(is_artist=True, is_staff=False)
        return context

class DetailRequest(DetailView):
    model = Member
    template_name = 'miembros/artist_detail.html'

def RejectRequest(request, pk):
    miembro = Member.objects.get(id=pk)
    if request.method == 'GET':
        miembro.is_artist = False
        miembro.is_staff = True
        miembro.save()
        return redirect('member:requests_list')
    return render(request, 'miembros/requests.html')

def AuthRequest(request, pk):
    miembro = Member.objects.get(id=pk)
    if request.method == 'GET':
        miembro.is_staff = True
        miembro.save()
        return redirect('member:requests_list')
    return render(request, 'miembros/requests.html')

def Follow(request, pk):
    artist = Member.objects.get(id=pk)
    follower = Member.objects.get(id=request.user.id)
    if request.method == 'GET':
        if(artist != follower):
            artist.members.add(follower)
            artist.save()
    return redirect('home:index')
    return render(request, 'agenda/home.html')

def Follow2(request, pk):
    artist = Member.objects.get(id=pk)
    follower = Member.objects.get(id=request.user.id)
    if request.method == 'GET':
        if(artist != follower):
            artist.members.add(follower)
            artist.save()
    return redirect('home:index2')
    return render(request, 'agenda/home2.html')
