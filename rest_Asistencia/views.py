from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt #crea un token
from core.models import Asistencia, Alumno
from .serializer import AsistenciaSerializer, AlumnoSerializer

# Create your views here.

@csrf_exempt
@api_view(['GET'])
def lista_asistencia(request):
    if request.method == 'GET':
        asistencia = Asistencia.objects.all()
        serializer = AsistenciaSerializer(asistencia, many=True)
        return Response(serializer.data)


@csrf_exempt
@api_view(['GET', 'POST'])
def usuario(request):
    if request.method == 'GET':
        usuarioAlumno = Alumno.objects.all()
        serializer = AlumnoSerializer(usuarioAlumno, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AlumnoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)