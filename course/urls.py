#define urls for the app
from django.urls import path
from . import views

urlpatterns = [
    path('create_user/', views.create_user, name='create_user'),
    path('update_user/<int:pk>/', views.update_user, name='update_user'),
    path('create_course/', views.create_course, name='create_course'),
    path('create_subject/', views.create_subject, name='create_subject'),
    path('subject_details/<int:pk>/', views.subject_details, name='subject_details'),
    path('course_details/<int:pk>/', views.course_details, name='course_details'),
]