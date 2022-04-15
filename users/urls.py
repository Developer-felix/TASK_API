#define urls for the app
from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.register, name='create_user'),
    path('user/<int:pk>/', views.update_user, name='update_user'),
]