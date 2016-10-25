from django.contrib import admin

from app.models import Artist, Category, Note, Event, User

# Register your models here.

admin.site.register(Artist)
admin.site.register(Event)
admin.site.register(Note)
