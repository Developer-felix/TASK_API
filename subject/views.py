from django.shortcuts import render
#import modules
from .serializers import SubjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Subject
#import status
from rest_framework import status
#import Acount
from users.models import Account
#import AcountSerializer
from users.serializers.users_serializer import AcountSerializer

def subject(request):
    if request.method == "GET":
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        data = request.data
        serializer = SubjectSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "errors": None, "status_code": 0,
                             "status_message": "successfully saved subject details",
                             "message": "You have successfully registered"}, status=status.HTTP_201_CREATED)
        return Response( {"success": False, "status_code": 1,
                              "status_message": "Cannot save subject details",
                              "message": "cannot save subject details","errors": serializer.errors, "data": None
                              },)
    return Response({"success"})


def subject_details(request, pk):
    if request.method == "DELETE":
        subject = Subject.objects.get(pk=pk)
        subject.delete()
        return Response({"success": True, "errors": None, "status_code": 0,
                         "status_message": "successfully deleted subject details",
                         "message": "You have successfully deleted subject details"}, status=status.HTTP_201_CREATED)
    if request.method == "GET":
        subject = Subject.objects.get(pk=pk)
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)
    elif request.method == "PUT":
        subject = Subject.objects.get(pk=pk)
        serializer = SubjectSerializer(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "errors": None, "status_code": 0,
                             "status_message": "successfully saved subject details",
                             "message": "You have successfully updated subject details"}, status=status.HTTP_201_CREATED)
        return Response({"success": False, "status_code": 1,
                         "status_message": "Cannot save subject details",
                         "message": "cannot save subject details", "errors": serializer.errors, "data": None
                         },)
    return Response({"success"})