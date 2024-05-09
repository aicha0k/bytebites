# created this file to add the urls for the ByteBites app
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home')
]