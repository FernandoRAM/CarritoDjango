from django.conf.urls import url, include
from django.contrib import admin
from apps.administrador import views

urlpatterns = [
	url(r'^admin', admin.site.urls),
]