from django import forms
from datetime import datetime

from app.models import Artist, Event, Note

class ArtistForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(datetime.today().year-80, datetime.today().year - 4)))
    class Meta:
        model = Artist

        fields = [
        'name',
        'last_name',
        'nickname',
        'password',
        'birth_date',
        'phone_number',
        'email',
        'address',
        'image_profile',
        'category',
        ]

        labels = {
        'name': 'Nombres',
        'last_name': 'Apellidos',
        'nickname': 'Usuario',
        'password': 'Contrasenia',
        'birth_date': 'Fecha de nacimiento',
        'phone_number': 'Numero de telefono',
        'email': 'Correo electronico',
        'address': 'Domicilio',
        'image_profile': 'Imagen de perfil',
        'category': 'Especialidad',
        }

class EventForm(forms.ModelForm):
    class Meta:

        model = Event

        fields = [
        'title',
        'description',
        'location',
        'date',
        'image_profile',
        'state',
        'categories',
        'arist',
        ]
        labels = {
        'title': 'Titulo',
        'description': 'Descripcion',
        'location': 'Ubicacion',
        'date': 'Fecha y Hora',
        'image_profile': 'Seleccionar imagen',
        'state': 'Estado Evento',
        'categories': 'Categoria',
        'arist': 'Artista',
        }
        widgets = {
        'title': forms.TextInput(attrs={'class':'form-control'}),
        'description': forms.Textarea(attrs={'class':'form-control'}),
        'location': forms.TextInput(attrs={'class':'form-control'}),
        'date': forms.SplitDateTimeWidget(),
        'image_profile': forms.FileInput(),
        'state': forms.RadioSelect(),
        'categories': forms.Select(),
        'arist': forms.Select(),
        }

class NoteForm(forms.ModelForm):
    class Meta:

        model = Note

        fields = [
        'title',
        'content',
        'category',
        'image_profile',
        ]

        labels = {
        'title': 'Titulo',
        'content': 'Contenido',
        'category': 'Categoria',
        'image_profile': 'Seleccionar imagen',
        }

        widgets = {
        'title': forms.TextInput(attrs={'class':'form-control'}),
        'content': forms.Textarea(attrs={'class':'form-control'}),
        'category': forms.Select(),
        'image_profile': forms.FileInput(),
        }
