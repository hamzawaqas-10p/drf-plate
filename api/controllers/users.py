#from django.shortcuts import render
#from rest_framework import viewsets

from api.models.users import User
from serializers.users_serializers import UserSerializer
from lib.base import Controller

# Create your views here.

class UserController(Controller):
    """
    This controller displays a list of all employees
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
