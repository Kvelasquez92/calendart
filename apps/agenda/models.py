from __future__ import unicode_literals

from django.db import models
from apps.miembros.models import Member
from apps.notas.models import Category

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=45, null=False, blank=False)
    description = models.TextField()
    location = models.CharField(max_length=45, null=False, blank=False)
    date = models.DateField()
    time = models.TimeField(blank=True, null=True)
    image_profile = models.ImageField(upload_to='events', blank=True, null=True)
    state_choice =(
        ('A', 'Activo'),
        ('F', 'Terminado'),
        ('C', 'Cancelado'),
    )
    state = models.CharField(max_length=1, null=False, blank=False, choices = state_choice, default='A')
    categories = models.ManyToManyField(Category, blank=False)
    members = models.ManyToManyField(Member, blank=True)
    def __str__(self):
        return self.title
