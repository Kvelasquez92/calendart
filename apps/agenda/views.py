from django.shortcuts import render
from apps.agenda.forms import EventForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView

# Create your views here.
def home(request):
    return render(request, 'agenda/home.html')

class EventCreate(CreateView):
    form_class = EventForm
    template_name = 'agenda/event_form.html'
    success_url = reverse_lazy('home:index')
