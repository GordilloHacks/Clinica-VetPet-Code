# Ejercicio/urls.py
from django.contrib import admin
from django.urls import path
from Ejercicio.vista import index, panel_inicio ,registro_inicio ,recu_contra , Condiciones

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('panel/', panel_inicio, name='panel_inicio'),
    path('Registro/', registro_inicio, name='registro_inicio'),
    path('Recu/', recu_contra, name='recuperar_contra'),
    path('Condiciones/', Condiciones, name='Terminos_Condiciones'),
]
