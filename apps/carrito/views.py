from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.conf import settings
from hola import models
from apps.administrador import models as ad
from apps.carrito import models

# Create your views here.

def inicio(request):
	hola = cargar()
	return render(request, 'inicio.html', hola)

def cargar():
	select = models.Producto.objects.all() 
	#print (select)
	diccionario = {}
	array = []
	for x in select:
		array.append([x.id,x.Nombre,x.Precio,x.Descripcion,x.idCategoria_id,x.idSucursal_id,x.Ruta])  

	diccionario["hola"] = array  
	return diccionario

def item(request, idP):
	diccionario={}
	array = []
	data = models.Producto.objects.filter(pk=idP).first()
	nombre = data.Nombre
	precio = data.Precio
	descripcion = data.Descripcion
	ruta = data.Ruta
	array.append([idP,nombre, precio, descripcion, ruta])
	diccionario["item"] = array
	return render(request, 'item.html', diccionario)

def log(request):
	return render(request, 'log.html')

def categorias(request, idC):
	array = []
	diccionario={}

	
	if idC is not None and idC == '' or idC =='0':
		print(idC)
		idC = 0
		categorias = ad.Categoria.objects.all();
		for i in categorias:
			array.append([idC,i.id, i.Nombre])
		diccionario["cate"] = array
		return render(request, 'categorias.html', diccionario)
	else:
		try:
			categorias = ad.Producto.objects.filter(idCategoria_id=idC);
			if len(categorias) > 0:
				for x in categorias:
					array.append([idC,x.id,x.Nombre,x.Precio,x.Descripcion,x.idCategoria_id,x.idSucursal_id,x.Ruta])
				diccionario["cate"] = array
				return render(request, 'categorias.html', diccionario)
			else:
				return render(request, 'errorSitio.html')

		except Exception as e:
			return render(request, 'errorSitio.html')
				
			
		


def registro(request):
	nombre = request.POST.get('nom') 
	mail = request.POST.get('mail') 
	pw = request.POST.get('pass')
	insert = models.Usuario(Nombre=nombre, Correo=mail, Pass=pw, TipoUsuario=2)
	if insert.save():
		return HttpResponse("1")
	else: 
		return HttpResponse("2")

def iniciar(request):
	mail = request.POST.get('mail') 
	pw = request.POST.get('pass')
	select = models.Usuario.objects.filter(Correo=mail, Pass=pw).first()
	if (select.Correo == mail and select.Pass == pw):
		return HttpResponse(select.Nombre)
	else: 
		return HttpResponse("2")
	
def error(request):
	return render(request, 'errorSitio.html')
	