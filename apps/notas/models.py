from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField( max_length=45, null=False, blank=False)
    description = models.TextField(blank = True)
    image_profile = models.ImageField(upload_to='categories', blank=True, null=True)
    def __str__(self):
        return self.name


class Note(models.Model):
    title = models.CharField(max_length=45, null=False, blank=False)
    content = models.TextField()
    category = models.ForeignKey(Category, null=False, blank = False, on_delete = models.CASCADE)
    image_profile = models.ImageField(upload_to='notes', blank=True, null=True)
    def __str__(self):
        return self.title
