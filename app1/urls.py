from django.urls import path
from . import views

urlpatterns = [
    path('' , views.inputy ,  name='home'),
    path('WordCount', views.count , name='count'),
    path('index', views.index , name='index'),
    path('register' , views.register , name='register'),
    path('login' , views.login , name='login'),
    path('logout' , views.logout , name='logout'),

]