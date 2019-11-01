from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('asesoria',views.asesoria,name="asesoria"),
    path('capacitacion',views.capacitacion,name="capacitacion"),
    path('about',views.about,name="about"),
    path('contacto',views.contacto,name="contacto")
]