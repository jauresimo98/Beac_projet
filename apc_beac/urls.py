from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('template', views.template, name='template'),
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

]