from django.urls import path
from rest_Asistencia.views import lista_asistencia, usuario

urlpatterns = [
    path('lista_asistencia/', lista_asistencia, name='lista de asistencia'),
    path('alumnos/', usuario, name='lista de usuarios')
    
]