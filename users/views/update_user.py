#import modules
from rest_framework.views import APIView
from rest_framework.response import Response
#import status
from rest_framework import status
#import Acount
from users.models import Account
#import AcountSerializer
from users.serializers.users_serializer import AcountSerializer

#write a view to update user in the AcountSerializer details

def update_user(request, pk):
    if request.method == "PUT":
        user = Account.objects.get(pk=pk)
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