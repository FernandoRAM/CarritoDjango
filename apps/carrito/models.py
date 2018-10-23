from django.db import models
from apps.administrador.models import Producto

class Usuario(models.Model):
	Nombre = models.CharField(max_length=50)
	Correo = models.CharField(max_length=50)
	Pass = models.CharField(max_length=300)
	TipoUsuario = models.IntegerField()

class Carrito(models.Model):
	Cantidad = models.IntegerField()
	Precio = models.IntegerField()
	idProducto = models.ForeignKey(Producto,on_delete=models.CASCADE,)
	idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,)




