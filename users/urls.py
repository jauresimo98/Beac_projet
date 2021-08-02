from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
#from .views import DashboardView
from django.contrib.auth.decorators import login_required
from django.conf.urls import url 

from django.contrib.auth.views import LoginView,LogoutView



urlpatterns = [
      path('connexion',views.login_connexion,name = 'connex'),
      path('',views.login_login,name = 'login_login'),
      path('register1',views.register,name = 'register1'),
      path('logout',views.logout_block,name = 'logout'),
]