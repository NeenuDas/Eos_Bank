from. import  views
from django.urls import path

urlpatterns = [
# path('',views.demo,name='demo'),
    path('', views.index, name='index'),
    path('home', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('app_form', views.app_form, name='app_form'),
    path('sucess', views.sucess, name='sucess'),
    ]