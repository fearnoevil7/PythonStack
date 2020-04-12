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
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
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
        # password = body['password']
        # pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        # print(pw_hash)
        # newUser = User.objects.create(username = str(random.randint(0,1000)), first_name = body['first_name'], last_name = body['last_name'], email = body['email'], password = pw_hash)
        # User.save(newUser)
        # print('account registered!!!!!!*********')
        
        # return JsonResponse({'message': 'user successfully created'})


        errors = User.objects.basic_validator(body)
        if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
                return JsonResponse({'error': errors})
        else:
            password1 = body['password']
            print("Passowrd!!!!!!", password1, type(password1))
            pw_hash = bcrypt.hashpw(password1.encode(), bcrypt.gensalt())
            print("********Hashed Password********", pw_hash)
            User.objects.create(username = body['name'], email = body['email'], password = pw_hash)
            print("User created******")
            # print(user1)
            return JsonResponse({'message': 'user successfully created'})

    # def get(self, request):
    #     return JsonResponse({'status': 'ok', 'users': list(User.objects.values().all())})

class session(View):
    def post(self, request):
        print("TEst!!!!!!!!!!!!!")
        body = json.loads(request.body.decode())
        # print(body, type(body))
        # user = User.objects.filter(email = body['email'])
        # if user:
        #     print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        #     logged_user = user[0]
        #     if bcrypt.checkpw(body['password'].encode(), logged_user.password.encode()):
        #         print("#######???????%%%%%%%%", logged_user)
        #         # userinfo = { 'email': logged_user.email, 'id': logged_user.id }
        #         # token = jwt.encode(userinfo, key, algorithm='HS256').decode()
        #         return JsonResponse({'message': 'user successfully logged in'})
        #     else:
        #         messages.error(request, "invalid password")
        #         return JsonResponse({'errors': 'invalid password'})
        # else:
        #     messages.error(request, "invalid email")
        #     return JsonResponse ({'errors': 'invalid email'})
        user = User.objects.filter(email = body['email'])
        if user:
            user1 = User.objects.get(email = body['email'])
            print("Test#1", user[0].password)
            print("Test#2!!!!!", body['password'].encode())
            logged_user = user[0]
            if bcrypt.checkpw(body['password'].encode(), user[0].password.encode()):
                userinfo = { 'email': logged_user.email, 'id': logged_user.id }
                token = jwt.encode(userinfo, key, algorithm='HS256').decode()
                return JsonResponse({'message': 'user successfully logged in'})
            else:
                messages.error(request, "invalid password")
                return JsonResponse({'errors': 'invalid password'})
        else:
            messages.error(request, "invalid email")
            return JsonResponse ({'errors': 'invalid email'})


# Create your views here.
