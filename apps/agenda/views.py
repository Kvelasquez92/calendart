from django.shortcuts import render
from apps.agenda.forms import EventForm
from apps.agenda.models import Event
from apps.notas.models import Category
from django.db.models import Count
from apps.miembros.models import Member
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

# Create your views here.

def Home(request):
    events = Event.objects.all().order_by('date')[:4]
    most_followed = Member.objects.annotate(member_count=Count('members')).filter(is_artist=True, is_staff=True).order_by('-member_count')[:4]
    count_followers =[]
    for artist in most_followed:
        count_followers.append(artist.members.count())
    most_followeds = zip(most_followed, count_followers)
    cats = Category.objects.all()
    bandera = True
    contexto = {'object_list':events, 'categorias':cats, 'bandera':bandera,'artistas':most_followeds, }
    return render(request, 'agenda/home.html', contexto)

def Home2(request, pk):
    sel_category = Category.objects.get(id=pk)
    events = Event.objects.all().order_by('date')
    cat_event = []
    counter = 1
    for event in events:
        for cat in event.categories.all():
            if cat == sel_category:
                cat_event.append(event)
                counter+=1
                break
        if counter==4:
            break
    most_followed = Member.objects.annotate(member_count=Count('members')).filter(is_artist=True, is_staff=True).order_by('-member_count')
    cat_artist = []
    counter = 1
    for artist in most_followed:
        for cat in artist.categories.all():
            if cat == sel_category:
                cat_artist.append(artist)
                counter+=1
                break
        if counter==4:
            break
    count_followers =[]
    for artist in most_followed:
        count_followers.append(artist.members.count())
    most_followeds = zip(cat_artist, count_followers)
    cats = Category.objects.all()
    contexto = {'object_list':cat_event, 'categorias':cats, 'cat':sel_category, 'artistas':most_followeds,}
    return render(request, 'agenda/home2.html', contexto)

class EventCreate(CreateView):
    form_class = EventForm
    template_name = 'agenda/event_form.html'
    success_url = reverse_lazy('home:index')

    def get_context_data(self, **kwargs):
        context = super(EventCreate, self).get_context_data(**kwargs)
        context['miembros'] = Member.objects.filter(is_artist=True)
        return context


def EventList(request):
    events = Event.objects.all().order_by('id')[:10]
    contexto = {'events':events}
    return render(request, 'agenda/event_list.html', contexto)

class DetalleEvento(DetailView):
    model = Event
    template_name = 'agenda/detalle_evento.html'

    def get_context_data(self, **kwargs):
        context = super(DetalleEvento, self).get_context_data(**kwargs)
        context['eventos'] = Event.objects.exclude(id = context['object'].id)[:2]
        return context
