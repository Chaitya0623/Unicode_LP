from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.createUser, name='Home'),
    path('update/<int:pk>/', views.updateUser, name='update'),
    path('delete/<int:pk>/', views.deleteUser, name='delete'),
]