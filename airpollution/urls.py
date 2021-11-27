from django.urls import path
from airpollution import views

urlpatterns = [
    path('', views.welcome, name='airpollution_welcome')
]