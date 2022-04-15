from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.serializers.users_serializer import Acount
from .models import Acount
from rest_framework.decorators import api_view
#import AccountSerializer
from .serializers.users_serializer import AcountSerializer


@api_view(["POST","GET"])
def register(request):
    if request.method == "GET":
        users = Acount.objects.all()
        serializer = AcountSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = AcountSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "errors": None, "status_code": 0,
                             "status_message": "successfully saved user details",
                             "message": "You have successfully registered"}, status=status.HTTP_201_CREATED)
        return Response( {"success": False, "status_code": 1,
                             "status_message": "Cannot save user details",
                             "message": "cannot save user details","errors": serializer.errors, "data": None
                             },)
    return Response({"success"})


#write a view to update user in the AcountSerializer details
@api_view(["PUT","DELETE"])
def update_user(request, pk):
    if request.method == "DELETE":
        user = Acount.objects.get(pk=pk)
        user.delete()
        return Response({"success": True, "errors": None, "status_code": 0,
                         "status_message": "successfully deleted user details",
                         "message": "You have successfully deleted user details"}, status=status.HTTP_201_CREATED)
                         
    if request.method == "PUT":
        user = Acount.objects.get(pk=pk)
        serializer = AcountSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "errors": None, "status_code": 0,
                             "status_message": "successfully saved user details",
                             "message": "You have successfully updated user details"}, status=status.HTTP_201_CREATED)
        return Response({"success": False, "status_code": 1,
                         "status_message": "Cannot save user details",
                         "message": "cannot save user details", "errors": serializer.errors, "data": None
                         },)