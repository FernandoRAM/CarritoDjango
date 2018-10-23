from django.db import models
import io
from django.core.files.base import File



class prueba(models.Model):
	item1 = models.CharField(max_length=50)
	item2 = models.FloatField()

class prueba2(models.Model):
	item3 = models.CharField(max_length=70)
	item4 = models.DateField()

class prueba3(models.Model):
	item5 = models.ForeignKey('prueba2')

class archivo(models.Model):
	nombre = models.CharField(max_length=100)
	archivo = models.FileField(upload_to='doc')

class imagen(models.Model):
	nombre = models.CharField(max_length=100)
	imagen = models.ImageField(upload_to = 'img')

class field(models.Model):
	imagen = models.FileField(upload_to='img')
	imagen2 = models.ImageField(upload_to='img')