from django.urls import path
from . import views

urlpatterns = [
    # Ejemplo de endpoint de prueba
    path('', views.home, name='api-home'),
]
