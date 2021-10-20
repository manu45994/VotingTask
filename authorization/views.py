from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.generics import GenericAPIView
from django.contrib.auth import authenticate
from django.conf import settings
import jwt

# Create your views here.



class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self,request):
        username = request.data.get("username","")
        password = request.data.get("password","")

        user = authenticate(username=username,password=password)

        if user is not None:
            auth_token = jwt.encode({"user":user.id},"secret",algorithm="HS256")

            serializer = UserSerializer(user)

            data = {"user":serializer.data,"token":auth_token}

            return Response(data,status=status.HTTP_200_OK)


