from django import forms

from app.models import Artist

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist

        fields = [
        'nickname',
        'name',
        'last_name',
        'birth_date',
        'phone_number',
        'email',
        'address',
        'image_profile',
        'category',
        ]

        labels = {
        'nickname': 'Usuario',
        'name': 'Nombres',
        'last_name': 'Apellidos',
        'birth_date': 'Fecha de nacimiento',
        'phone_number': 'Numero de telefono',
        'email': 'Correo electronico',
        'address': 'Domicilio',
        'image_profile': 'Imagen de perfil',
        'category': 'Especialidad',
        }

        widgets = {
        'nickname': forms.TextInput(attrs={'class':'form-control'}),
        'name': forms.TextInput(attrs={'class':'form-control'}),
        'last_name': forms.TextInput(attrs={'class':'form-control'}),
        'birth_date': forms.TextInput(attrs={'class':'form-control'}),
        'phone_number': forms.TextInput(attrs={'class':'form-control'}),
        'email': forms.TexInput(attrs={'class':'form-control'}),
        'address': forms.Textarea(attrs={'class':'form-control'}),
        'image_profile': forms.FileField(attrs={'class':'form-control'}),
        'category': forms.CheckboxSelectMultiple(),
        }
