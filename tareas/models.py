
# Create your models here.
from django.db import models


class Tarea(models.Model):
    ESTADOS = [
        ("pendiente", "Pendiente"),
        ("en_progreso", "En progreso"),
        ("completada", "Completada"),
    ]

    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    responsable = models.CharField(max_length=100, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_limite = models.DateField(null=True, blank=True)
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default="pendiente",
    )

    def __str__(self):
        return self.titulo