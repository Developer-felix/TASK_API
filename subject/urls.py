#define urls for the app
from django.urls import path
#import register from create_user.py
from . import views

urlpatterns = [
    path('subject/', views.subject, name='create_user'),
    path('subject/<int:pk>/', views.subject_details, name='update_user'),
]