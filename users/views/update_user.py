#import modules
from rest_framework.views import APIView
from rest_framework.response import Response
#import status
from rest_framework import status
#import Acount
from users.models import Account
#import AcountSerializer
from users.serializers.users_serializer import AcountSerializer
