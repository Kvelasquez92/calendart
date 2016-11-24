# -*- coding: utf-8 -*-
u'ñó'

from django import forms
from datetime import datetime
from apps.miembros.models import Member
from django.contrib.auth.forms import UserCreationForm


class MemberForm(UserCreationForm):
    class Meta:
        model = Member

        fields = [
            'username',
            'first_name',
            'last_name',
            'date_of_birth',
            'email',
            'address',
        ]

        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'date_of_birth': 'Fecha de nacimiento',
            'email': 'Correo electronico',
            'address': 'Dónde vives?',
        }

        widgets = {
            'date_of_birth':forms.SelectDateWidget(years=range(datetime.today().year-80, datetime.today().year - 4))
        }

class ArtistForm(forms.ModelForm):
    class Meta:
        model=Member

        fields = [
            'biography',
            'phone_number',
            'date_of_birth',
            'image_profile',
            'categories',
        ]

        widgets = {
            'date_of_birth':forms.SelectDateWidget(years=range(datetime.today().year-80, datetime.today().year - 4))
        }

class ArtistProfileForm(forms.ModelForm):
    class Meta:
        model = Member

        fields = [
            'username',
            'first_name',
            'last_name',
            'date_of_birth',
            'email',
            'address',
            'biography',
            'phone_number',
            'date_of_birth',
            'image_profile',
            'categories',
        ]

        widgets = {
            'date_of_birth':forms.SelectDateWidget(years=range(datetime.today().year-80, datetime.today().year - 4))
        }
