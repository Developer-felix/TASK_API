#define urls for the app
from django.urls import path
from . import views

urlpatterns = [
    path('create_user/', views.register, name='create_user'),
    path('update_user/<int:pk>/', views.update_user, name='update_user'),
]