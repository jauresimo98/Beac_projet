from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('apc_beac/', include('apc_beac.urls')),

]