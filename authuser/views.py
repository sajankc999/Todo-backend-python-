from django.shortcuts import render,HttpResponse
from rest_framework.viewsets import ModelViewSet,generics
from django.contrib.auth import get_user_model
from .serializers import *
from rest_framework.response import Response
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view 
user = get_user_model()
# Create your views here.


class Register(generics.CreateAPIView):
    queryset = user.objects.all()
    serializer_class = RegisterSerializer

    # def post(self,request,*args, **kwargs):


# class Login(generics.RetrieveAPIView):
#     queryset = user.objects.all()
#     serializer_class = LoginSerializer
    
@api_view(['POST'])
def login(request):
    data = request.data
    email = data.get('email')
    password = data.get('password')
    user = authenticate(username = email,password=password)
    if user:
        token,_ = Token.objects.get_or_create(user=user)
        return Response({
            "username":user.get_username(),
            "token":token.key,
        })
    return  Response(user)

