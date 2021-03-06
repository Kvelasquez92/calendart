from django.db import models
import os

# Create your models here.
def get_artist_image_path(instance, filename):
    if instance.id is None:
        return os.path.join('artists', str(1), filename)
    else:
        return os.path.join('artists', str(instance.id), filename)

def get_event_image_path(instance, filename):
    if instance.id is None:
        return os.path.join('events', str(1), filename)
    else:
        return os.path.join('events', str(instance.id), filename)

def get_note_image_path(instance, filename):
    if instance.id is None:
        return os.path.join('notes', str(1), filename)
    else:
        return os.path.join('notes', str(instance.id), filename)

def get_category_image_path(instance, filename):
    if instance.id is None:
        return os.path.join('categories', str(1), filename)
    else:
        return os.path.join('categories', str(instance.id), filename)

class Category(models.Model):
    name = models.CharField( max_length=45, null=False, blank=False)
    description = models.TextField(blank = True)
    image_profile = models.ImageField(upload_to='categories', blank=True, null=True)
    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=45, null=False, blank=False)
    last_name = models.CharField(max_length=45, null=False, blank=False)
    nickname =  models.CharField(max_length=45, null=False, blank=False)
    password = models.CharField(max_length=20, null=False, blank=False)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=254, null=False, blank=False)
    address = models.CharField(max_length=150, null=True, blank=True)
    image_profile = models.ImageField(upload_to='artists', blank=True, null=True)
    is_active = models.BooleanField(null=False, blank=False, default=False)
    category = models.ForeignKey(Category, null=True, blank = True, on_delete = models.CASCADE)
    def __str__(self):
        return self.nickname

class Note(models.Model):
    title = models.CharField(max_length=45, null=False, blank=False)
    content = models.TextField()
    category = models.ForeignKey(Category, null=False, blank = False, on_delete = models.CASCADE)
    image_profile = models.ImageField(upload_to='notes', blank=True, null=True)
    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=45, null=False, blank=False)
    description = models.TextField()
    location = models.CharField(max_length=45, null=False, blank=False)
    date = models.DateTimeField()
    image_profile = models.ImageField(upload_to='events', blank=True, null=True)
    state_choice =(
        ('A', 'Activo'),
        ('F', 'Terminado'),
        ('C', 'Cancelado'),
    )
    state = models.CharField(max_length=1, null=False, blank=False, choices = state_choice, default='A')
    categories = models.ManyToManyField(Category, blank=True)
    arist = models.ManyToManyField(Artist, blank=True)
    def __str__(self):
        return self.title

class User(models.Model):
    nickname = models.CharField(max_length=45, null = False, blank = False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    genre_choice = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    )
    genre = models.CharField(max_length=1, null = True, blank=False, choices = genre_choice)
    arist = models.ManyToManyField(Artist)
    event = models.ManyToManyField(Event)
    def __str__(self):
        return self.nickname
