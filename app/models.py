from django.db import models
import os

# Create your models here.
def get_artist_image_path(instance, filename):
    if instance.id is None:
        return os.path.join('media/artists', str(1), filename)
    else:
        return os.path.join('media/artists', str(instance.id), filename)

def get_event_image_path(instance, filename):
    if instance.id is None:
        return os.path.join('media/events', str(1), filename)
    else:
        return os.path.join('media/events', str(instance.id), filename)

def get_note_image_path(instance, filename):
    if instance.id is None:
        return os.path.join('media/notes', str(1), filename)
    else:
        return os.path.join('media/notes', str(instance.id), filename)

def get_category_image_path(instance, filename):
    if instance.id is None:
        return os.path.join('media/categories', str(1), filename)
    else:
        return os.path.join('media/categories', str(instance.id), filename)

class Category(models.Model):
    name = models.CharField('Nombre de la categoria', max_length=45, null=False, blank=False)
    description = models.TextField('Descripcion de la categoria', blank = True)
    image_profile = models.ImageField(upload_to=get_category_image_path, blank=True, null=True)
    def __str__(self):
        return self.name

class Artist(models.Model):
    nickname =  models.CharField('Nombre de usuario' ,max_length=45, null=False, blank=False)
    name = models.CharField('Nombre', max_length=45, null=False, blank=False)
    last_name = models.CharField('Apellido', max_length=45, null=False, blank=False)
    birth_date = models.DateField('Fecha de nacimiento')
    phone_number = models.CharField('Numero de telefono', max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=254, null=False, blank=False)
    address = models.CharField(max_length=150, null=True, blank=True)
    image_profile = models.ImageField(upload_to=get_artist_image_path, blank=True, null=True)
    is_active = models.BooleanField(null=False, blank=False, default=True)
    category = models.ForeignKey(Category, null=True, blank = True, on_delete = models.CASCADE)
    def __str__(self):
        return self.nickname

class Note(models.Model):
    title = models.CharField(max_length=45, null=False, blank=False)
    content = models.TextField()
    category = models.ForeignKey(Category, null=False, blank = False, on_delete = models.CASCADE)
    image_profile = models.ImageField(upload_to=get_note_image_path, blank=True, null=True)
    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=45, null=False, blank=False)
    description = models.TextField('Descripcion del evento')
    location = models.CharField(max_length=45, null=False, blank=False)
    date = models.DateTimeField()
    image_profile = models.ImageField(upload_to=get_event_image_path, blank=True, null=True)
    Active = 'A'
    Finished = 'F'
    Canceled = 'C'
    state_choice =(
        (Active, 'Activo'),
        (Finished, 'Terminado'),
        (Canceled, 'Cancelado'),
    )
    state = models.CharField(max_length=1, choices = state_choice, default = Active)
    categories = models.ManyToManyField(Category)
    arist = models.ManyToManyField(Artist)
    def __str__(self):
        return self.title

class User(models.Model):
    nickname = models.CharField(max_length=45, null = False, blank = False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    male = 'M'
    female = 'F'
    other = 'O'
    genre_choice = (
        (male, 'Masculino'),
        (female, 'Femenino'),
        (other, 'Otro'),
    )
    genre = models.CharField(max_length=1, null = True, blank=False, choices = genre_choice)
    arist = models.ManyToManyField(Artist)
    event = models.ManyToManyField(Event)
    def __str__(self):
        return self.nickname
