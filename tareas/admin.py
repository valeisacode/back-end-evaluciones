from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Tarea


@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "responsable",
        "estado",
        "fecha_limite",
    )
    list_filter = ("estado",)
    search_fields = ("titulo", "descripcion", "responsable")
