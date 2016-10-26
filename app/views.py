from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from app.forms import ArtistForm
from app.models import Artist

# Create your views here.

class ArtistCreate(CreateView):
    model = Artist
    form_class = ArtistForm
    template_name = 'app/artista_form.html'
    success_url = reverse_lazy('artist:artist_create')

def home(request):
    return render(request, 'app/home.html')
