from django.shortcuts import render
from .serializers import CourseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course
#import status
from rest_framework import status
from rest_framework.decorators import api_view

#create view for course using function based views CourseSerializer
@api_view(['GET', 'POST'])
def course(request):
    if request.method == "GET":
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        data = request.data
        serializer = CourseSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "errors": None, "status_code": 0,
                             "status_message": "successfully saved course details",
                             "message": "You have successfully registered"}, status=status.HTTP_201_CREATED)
        return Response( {"success": False, "status_code": 1,
                              "status_message": "Cannot save course details",
                              "message": "cannot save course details","errors": serializer.errors, "data": None
                              },)

    return Response({"success"})

@api_view(["DELETE", "PUT"])
def course_detail(request, pk):
    if request.method == "DELETE":
        course = Course.objects.get(pk=pk)
        course.delete()
        return Response({"success": True, "errors": None, "status_code": 0,
                         "status_message": "successfully deleted course details",
                         "message": "You have successfully deleted course details"}, status=status.HTTP_201_CREATED)
    if request.method == "PUT":
        course = Course.objects.get(pk=pk)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "errors": None, "status_code": 0,
                             "status_message": "successfully saved course details",
                             "message": "You have successfully updated course details"}, status=status.HTTP_201_CREATED)
        return Response({"success": False, "status_code": 1,
                         "status_message": "Cannot save course details",
                         "message": "cannot save course details", "errors": serializer.errors, "data": None
                         },)