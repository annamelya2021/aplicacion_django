from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path("adios/", views.adios),
    path("dime_fecha/", views.devuelve_fecha),
    path('agregar_usuario/', views.agregar_usuario, name='agregar_usuario'),
    path('agregar_material/', views.agregar_material, name='agregar_material'),
    path('lista_usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('lista_materiales/', views.lista_materiales, name='lista_materiales'),
    path('lista_prestamos/', views.lista_prestamos, name='lista_prestamos'),
]