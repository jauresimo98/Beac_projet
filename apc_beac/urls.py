from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
<<<<<<< HEAD
    path('template', views.template, name='template'),
=======
<<<<<<< HEAD: objec
HEAD

=======
>>>>>>> 6dac6e872963eb99451e830837851202c5b9c1ad
    path('input', views.simple_upload, name='input'),
    path('periode', views.periode, name='periode'),
    path('recupere_periode', views.recupere_periode, name='recupere_periode'),
    path('mvt/', views.liste_mvt, name='mvt_list'),
    path('mvt/ADD/', views.creer_mvt, name='mvt_create'),
    path('mvt/(?P<pk>\d+)/update/$', views.modifier_mvt, name='mvt_update'),
    path('tiers/', views.liste_tiers, name='tiers_list'),
    path('tiers/ADD/', views.creer_tiers, name='tiers_create'),
    path('tiers/(?P<pk>\d+)/update/$', views.modifier_tiers, name='tiers_update'),
    path('create-pdf', views.pdf_report_create,name='create-pdf'),
    
>>>>>>> ed8ede5b02c958b978456b483604be6b6a1db5c8

]