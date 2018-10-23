from django.conf.urls import url, include
from django.contrib import admin
from apps.carrito import views

urlpatterns = [
	url(r'^$', views.inicio, name="inicio"),
	url(r'^/log$', views.log, name="log"),
	url(r'^/categorias/(?P<idC>.*)$', views.categorias, name="categorias"),
	url(r'^/registro$', views.registro, name="registro"),
	url(r'^/iniciar$', views.iniciar, name="iniciar"),
	url(r'^/item/(?P<idP>.*)$', views.item, name="item"),
]