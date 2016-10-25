from django.db import models

# Create your models here.

def get_image_path(instance, filename):
    return os.path.join('products', str(instance.id), filename)

class Category(models.Model):
    name = models.CharField('Nombre de la categoría', max_length=45, null=False, blank=False)
    description = models.TextField('Descripcion de la categoría', blank = True)
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
    image_profile = models.ImageField
    is_active = models.BooleanField(null=False, blank=False, default=True)
    category = models.ForeignKey(Category, null=True, blank = False, on_delete = models.CASCADE)
    def __str__(self):
        return self.nickname

class Event(models.Model):
    title = models.CharField('Titulo del evento', max_length=45, null=False, blank=False)
    description = models.TextField('Descripción del evento')
    location = models.CharField('Lugar del evento', max_length=45, null=False, blank=False)
    date = models.DateTimeField('Fecha y hora')
    #image event
    Active = 'A'
    Finished = 'F'
    Canceled = 'C'
    state_choice =(
        (Active, 'Activo'),
        (Finished, 'Terminado'),
        (Canceled, 'Cancelado'),
    )
    state = models.CharField('Estado del evento', max_length=1, choices = state_choice, default = Active)
    categories = models.ManyToManyField(Category)
    arist = models.ManyToManyField(Artist)
    def __str__(self):
        return self.title

class Note(models.Model):
    title = models.CharField(max_length=45, null=False, blank=False)
    content = models.TextField()
    category = models.ForeignKey(Category, null=False, blank = False, on_delete = models.CASCADE)
    def __str__(self):
        return self.title

class User(models.Model):
    nickname = models.CharField('Nombre de usuario', max_length=45, null = False, blank = False)
    email = models.EmailField('Email', max_length=254, null=False, blank=False)
    male = 'M'
    female = 'F'
    other = 'O'
    genre_choice = (
        (male, 'Masculino'),
        (female, 'Femenino'),
        (other, 'Otro'),
    )
    genre = models.CharField('Genero', max_length=1, null = True, blank=False, choices = genre_choice)
    arist = models.ManyToManyField(Artist)
    event = models.ManyToManyField(Event)
    def __str__(self):
        return self.nickname
