from django.conf.urls import url
from hola import views

urlpatterns = [
    url(r'^$', views.index_view, name="index_view"),
    url(r'^lol$', views.lol, name="lol"),
    url(r'^lol/update$', views.pruebaUpdate, name="pruebaUpdate"),
    url(r'^lol/registro$', views.registro, name="registro"),
    url(r'^lol/formulario$', views.formulario_view, name="formulario"),
    url(r'^lol/data$', views.data, name="data"),
    url(r'^lol/image$', views.image, name="image"),
]
	
