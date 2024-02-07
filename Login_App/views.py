from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from .Serializers import SerializerUser
from django.http import HttpResponse

# Create your views here.

class UserViews(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SerializerUser
    
def LayoutInit(request):
    return HttpResponse('<center><h1>Welcome to the django Back-End Environment</h1></center><hr/><br/><center><h3>Here will appear the datas of the uers from your project</h3><br/><br/><img src="https://maxmautner.com/public/images/django.gif" alt="django"/></center>')