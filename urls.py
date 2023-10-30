from django.urls import path
from . import views

urlpatterns = [
    path('calcular_descuento/', views.calcular_descuento, name='calcular_descuento'),
]

from django.urls import path
from . import views

urlpatterns = [
    # Otras URLs de la aplicación
    path('', views.homepage, name='homepage'),
]
