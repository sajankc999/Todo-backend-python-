from django.shortcuts import render
from .models import *
from rest_framework.viewsets import generics,ModelViewSet
from .serializer import TaskSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class TaskViewset(ModelViewSet):
    model = Task.objects.all()
    serializer_class= TaskSerializer
    permission_classes =[IsAuthenticated,]
    def get_queryset(self):

        return Task.objects.filter(author = self.request.user)
    

class CollabTaskViewset(ModelViewSet):
    model = Task.objects.all()
    serializer_class= TaskSerializer
    permission_classes =[IsAuthenticated,]
    def get_queryset(self):

        return Task.objects.filter(collaborative_users = self.request.user)