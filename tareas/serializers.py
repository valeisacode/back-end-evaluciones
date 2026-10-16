from rest_framework import serializers

from .models import Tarea


class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = [
            "id",
            "titulo",
            "descripcion",
            "responsable",
            "fecha_creacion",
            "fecha_limite",
            "estado",
        ]
        read_only_fields = ["id", "fecha_creacion"]

    def validate_titulo(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "El título no puede estar vacío."
            )

        return value