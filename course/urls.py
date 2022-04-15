#define urls for the app
from django.urls import path
from . import views

urlpatterns = [
    path('create_user/', views.course, name='create_user'),
    path('update_user/<int:pk>/', views.course_detail, name='update_user'),
    path('create_course/', views.course, name='create_course'),
    path('course_details/<int:pk>/', views.course_detail, name='course_details'),
]