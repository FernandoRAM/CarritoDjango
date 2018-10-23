from django.db import models

class Sucursal(models.Model):
	Nombre = models.CharField(max_length=50)
	Direccion = models.CharField(max_length=100)

class Producto(models.Model):
	Nombre = models.CharField(max_length=50)
	Precio = models.DecimalField(max_digits=5, decimal_places=3)
	Descripcion = models.CharField(max_length=300)
	Ruta = models.CharField(max_length=300)
	idSucursal = models.ForeignKey('Sucursal')
	idCategoria = models.ForeignKey('Categoria')
	
class Categoria(models.Model):
	Nombre = models.CharField(max_length=50)
