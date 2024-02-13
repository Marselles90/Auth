from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('auth/', views.auth, name='auth'),
    path('exit/', views.exit, name='exit'),
    path('transaction/', views.transaction, name='transaction'),
    ]