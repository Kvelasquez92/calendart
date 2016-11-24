from __future__ import unicode_literals

from django.db import models
from apps.notas.models import Category
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import unittest

# Create your models here.

class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            return ValueError('El email es un campo obligatorio.')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, is_active=True, is_staff=is_staff, is_superuser=is_superuser, **extra_fields )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, True, True, **extra_fields)

class Member(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique = True)
    email = models.EmailField(max_length=50, unique = True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_artist = models.BooleanField(default=False)
    date_of_birth = models.DateField()
    biography = models.TextField(blank = True, null = True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    image_profile = models.ImageField(upload_to='members', default='members/default.jpg')
    categories = models.ManyToManyField(Category, blank=False)
    members = models.ManyToManyField('Member', blank = True)
    def __str__(self):
        return self.username


    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        return self.first_name, self.last_name

    def get_short_name(self):
        return self.username

    def presentacion(self):
        return 'Soy ' + self.first_name + ' y me dicen ' + self.username + ', vivo en ' + self.address
