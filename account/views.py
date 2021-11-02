import random
import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
class RegisterAPIView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = User.objects.create_user(
            username=username,
            email='dok@gmail.com',
            password=password,
            is_active=False
        )
        code = str(random.randint(1000, 9999))
        valid_until = datetime.datetime.now() + datetime.timedelta(minutes=20)
        Confirmcode.objects.create(user=user, code=code, valid_until=valid_until)
        # send_code_to_phone(code, username)
        return Response(data={'message': 'user created!'})
class ConfirmAPIView(APIView):
    def post(self, request):
        code = request.data['code']
        code_list = Confirmcode.objects.filter(code=code, valid_until__gte=datetime.datetime.now())

        if code_list:
            user = code_list[0]
            user.is_active = True
            user.save()
            return Response(data={'message': 'user activated'})
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)