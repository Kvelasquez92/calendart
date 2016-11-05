from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from app.forms import ArtistForm, NoteForm, EventForm
from app.models import Artist, Event, Note

# Create your views here.

def home(request):
    return render(request, 'app/home.html')


class ArtistCreate(CreateView):
    model = Artist
    form_class = ArtistForm
    template_name = 'app/artista_form.html'
    success_url = reverse_lazy('artist:artist_create')

class ArtistList(ListView):
    model = Artist
    template_name = 'app/artist_list.html'

class ArtistUpdate(UpdateView):
    model = Artist
    form_class = ArtistForm
    template_name = 'app/artista_form.html'
    success_url = reverse_lazy('artist:inicio')

class NoteCreate(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'app/note_form.html'
    success_url = reverse_lazy('home:index')
