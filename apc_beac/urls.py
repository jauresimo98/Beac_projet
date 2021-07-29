from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
<<<<<<< HEAD

=======
    path('input', views.simple_upload, name='input'),
    path('periode', views.periode, name='periode'),
    path('recupere_periode', views.recupere_periode, name='recupere_periode'),
    
>>>>>>> ed8ede5b02c958b978456b483604be6b6a1db5c8

]