from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('input', views.simple_upload, name='input'),
    path('periode', views.periode, name='periode'),
    path('recupere_periode', views.recupere_periode, name='recupere_periode'),

]