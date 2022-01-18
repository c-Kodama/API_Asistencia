from rest_framework import serializers
from core.models import Alumno, Asistencia

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ['id_alumno', 'rut', 'usuario', 'contrasena','asistencia']

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = ['id_asistencia', 'rut_alumno', 'codigo_asignatura', 'nombre_asignatura', 'fecha', 'seccion', 'sede', 'escuela', 'docente']