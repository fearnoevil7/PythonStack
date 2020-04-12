from django.shortcuts import render
import random
from django.views import View
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib import messages
import bcrypt
import json
import jwt
from .models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
key = 'secret'

class user(View):
    def post(self,request):
        print("Testing!!!!!!!!")
        body = json.loads(request.body.decode())
        print(body, type(body))
        # errors = User.objects.basic_validator(body)
        # if len(errors) > 0:
        #     for key, value in errors.items():
        #         messages.error(request, value)
        #     return JsonResponse({'error': errors})
        # else:
        password = body['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        print(pw_hash)
        user = User.objects.create(username = str(random.randint(0,1000)), first_name = body['first_name'], last_name = body['last_name'], email = body['email'], password = pw_hash)
        print('account registered!!!!!!*********')
        print(user.username)
        print(user.first_name)
        print(user.last_name)
        print(user.email)
        print(user.password)
        return JsonResponse({'message': 'user successfully created'})


