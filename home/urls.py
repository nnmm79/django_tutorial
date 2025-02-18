from django.contrib import admin
from django.urls import path

from home import views

urlpatterns = [ 
    path('', views.HomeView.as_view(), name = 'home'),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),
    path('test', views.LogoutInterfaceView.as_view(), name='test'),
    path('signup', views.SignupView.as_view(), name='signup'),
]
