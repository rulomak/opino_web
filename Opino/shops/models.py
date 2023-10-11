from django.db import models
from django.utils.timezone import now



# categorias 
class Category(models.Model):
    name_cat = models.CharField(max_length=70, null=False, blank=False)

    def __str__(self):
        return self.name_cat

# ciudades
class City(models.Model):
    name_city = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name_city

# paises 
class Country(models.Model):
    name_country = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return self.name_country


def user_directory_path(instance, filename):
   return 'blog/{0}/{1}'.format(instance.title, filename)


class Post(models.Model):
    nombre = models.CharField(max_length=300, default="sin registro")
    direccion = models.CharField(max_length=250, null=False)
    ciudad = models.CharField(max_length=250, null=True)
    published = models.DateTimeField(default=now)
    telefono = models.CharField(max_length=30, null=True)
    latitud = models.CharField(max_length=20, null=True)
    longitud = models.CharField(max_length=20, null=True)
    web = models.CharField(max_length=60, null=True)
    puntuacion = models.CharField(max_length=5, null=False, default=0)
    imagen =  models.ImageField(upload_to="blog", null=True, blank=True)
    slug = models.SlugField(max_length=550, unique_for_date='published', null=False, unique=True)
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    ciudad_id = models.ForeignKey(City, on_delete=models.CASCADE, default=1)
    pais = models.ForeignKey(Country, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nombre
