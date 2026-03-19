from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contacto/', views.contacto, name="contacto"),
    path('acerca_de/', views.acerca_de, name="acerca_de"),
    path('invitacion/', views.pasaporte_amor, name="pasaporte"),
]