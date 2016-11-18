# -*- coding: utf-8 -*-
u'íó'

from django import forms
from datetime import datetime
from apps.agenda.models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title',
            'description',
            'location',
            'date',
            'time',
            'image_profile',
            'categories',
            'members',
        ]

        labels = {
            'title': 'Título del Evento',
            'description': 'Descripción',
            'location': 'Ubicación',
            'date': 'Fecha',
            'time': 'Hora',
            'image_profile': 'Foto de Portada',
            'categories': 'Categorías',
            'members': 'Artistas Participantes',
        }
        widgets = {
            'date':forms.SelectDateWidget(years=range(datetime.today().year, datetime.today().year + 4)),
            'categories':forms.CheckboxSelectMultiple(),
            'members':forms.CheckboxSelectMultiple(),
        }
