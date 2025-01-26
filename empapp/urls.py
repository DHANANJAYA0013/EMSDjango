from django.contrib import admin
from django.urls import path
from empapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view', views.view, name='view'),
    path('add', views.add, name='add'),
    path('remove/<int:e_id>', views.remove, name='remove'),
    path('remove', views.remove, name='remove'),
    path('filter', views.filter, name='filter'),
]
