from django.test import TestCase
from apps.agenda.models import Event
from apps.agenda.forms import EventForm
from apps.notas.models import Category
from apps.miembros.models import Member

# Create your tests here.

class AgendaTestCase(TestCase):

    def test_valid_form(self):
        datos = {'title': 'Evento3', 'description': "Descripcion de evento 3", 'location': 'parque xela', 'date': '2016-12-20', 'time': '', 'image_profile': ''} #Los fields del form
        form = EventForm(data=datos)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        e = Event.objects.create(title='Evento2', description = "description de evento 2", location = 'democracia xela', date = '2016-12-24', state = 'A')
        datos = {'title': e.title, 'description': e.description, 'location': e.location, 'date': '2016-13-24', 'time': e.time, 'image_profile': e.image_profile,}
        form = EventForm(data=datos)
        self.assertFalse(form.is_valid())
