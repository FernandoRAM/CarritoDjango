from django.shortcuts import render
from hola import models 
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# Create your views here.
def index_view(request):
	select = models.prueba2.objects.all() 
	diccionario = {}
	array = []
	for x in select:
		array.append([x.item3,x.item4])  

	diccionario["hola"] = array  
	return render(request, 'prueba.html', diccionario)
	#return JsonResponse(data)

def lol(request):
	test = models.prueba2(item3 = 'PRUEBA', item4 ='2018-08-21')
	test.save()
	return HttpResponse(1)

def pruebaUpdate(request):
	update = models.prueba2.objects.filter(pk=3).first()
	update.item3 = 'cambio'
	update.item4 = '2018-08-30'  
	update.save()
	return HttpResponse(update.pk)

def registro(request):
	user = request.POST.get('user') 
	passw = request.POST.get('pass') 
	return HttpResponse(user+"/"+passw)

def formulario_view(request):
	return render(request, 'formulario.html')

def data(request):
	img = request.FILES['img']
	test = models.imagen(nombre = img, imagen =img)
	test.save()
	return HttpResponse(1)

def image(request):
	select = models.imagen.objects.all()
	diccionario = {}
	array = []
	for x in select:
		array.append([x.imagen,x.nombre])  

	diccionario["hola"] = array  
	return render(request, 'formulario.html', diccionario)
