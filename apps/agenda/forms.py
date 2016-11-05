# -*- coding: utf-8 -*-
u'íó'

from django import forms
from datetime import datetime
from apps.agenda.models import Event
from apps.notas.models import Category
from apps.miembros.models import Member

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title',
            'description',
            'location',
            'date',
            'image_profile',
            'categories',
            'members',
        ]

        labels = {
            'title': 'Título del Evento',
            'description': 'Descripción',
            'location': 'Ubicación',
            'date': 'Fecha',
            'image_profile': 'Foto de Portada',
            'categories': 'Categorías',
            'members': 'Artistas Participantes',
        }
        widgets = {
            'date':forms.SelectDateWidget(years=range(datetime.today().year, datetime.today().year + 4)),
            'categories':forms.CheckboxSelectMultiple(),
            'members':forms.CheckboxSelectMultiple(), 
        }
