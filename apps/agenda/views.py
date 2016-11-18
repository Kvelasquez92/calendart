from django.shortcuts import render
from apps.agenda.forms import EventForm
from apps.agenda.models import Event
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView

# Create your views here.

class Home(ListView):
    template_name = 'agenda/home.html'
    model = Event

class EventCreate(CreateView):
    form_class = EventForm
    template_name = 'agenda/event_form.html'
    success_url = reverse_lazy('home:index')


def EventList(request):
    events = Event.objects.all().order_by('id')[:10]
    contexto = {'events':events}
    return render(request, 'agenda/event_list.html', contexto)
