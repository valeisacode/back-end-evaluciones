
from django.shortcuts import render

def inicio(request):
    # Reemplaza 'index.html' por el nombre exacto del archivo que creaste dentro de tareas/templates/
    return render(request, 'index.html')

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Tarea
from .serializers import TareaSerializer


def inicio(request):
    return render(request, "index.html")


class TareaViewSet(ModelViewSet):
    queryset = Tarea.objects.all().order_by("-fecha_creacion")
    serializer_class = TareaSerializer
