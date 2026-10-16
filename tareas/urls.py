from django.urls import path
from . import views

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import inicio, TareaViewSet

app_name = "tareas"

router = DefaultRouter()
router.register("tareas", TareaViewSet, basename="tarea")

urlpatterns = [
    path("", inicio, name="inicio"),
    path("api/", include(router.urls)),
]