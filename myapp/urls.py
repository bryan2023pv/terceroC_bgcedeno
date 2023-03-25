from django.urls import path
from . import views

urlpatterns = [
    path('', views.homedef),

    path('edicionCurso/<codigo>', views.edicionCurso),
    path('editarCurso/', views.editarCurso),
    path('eliminarCurso/<codigo>', views.eliminarCurso),
]