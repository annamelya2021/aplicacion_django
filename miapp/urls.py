from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path("adios/", views.adios),
    path("dime_fecha/", views.devuelve_fecha),
]