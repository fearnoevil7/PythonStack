from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import Task, User
from django.contrib import messages
import bcrypt
import jwt
from rest_framework.permissions import IsAuthenticated 
# from rest_framework import viewsets
# from django.contrib.auth.models import User
# from .serializers import UserSerializer
import json
key = 'secret'

class task(View):
    def get(self, request):
        return JsonResponse({'status': 'ok', 'tasks': list(Task.objects.values().all())})
    def post(self, request):
        body = json.loads(request.body.decode())
        print(body, type(body))
        new_task = Task.objects.create(description = body['description'], isCompleted = body['isCompleted'])
        print(new_task)
        return JsonResponse({'status': 'ok'})
    def delete(self, request, task_id):
        print("Hoooraaaayyyyy")
        print(task_id)
        task1 = Task.objects.get(id=task_id)
        task1.delete()
        return JsonResponse({'status': 'ok'})
    
class show(View):
    def delete(self, request, task_id):
        print("Hoooraaaayyyyy")
        print(task_id)
        task1 = Task.objects.get(id=task_id)
        task1.delete()
        return JsonResponse({'status': 'ok'})

    def get(self, request, task_id):
        print("Testing123")
        task2 = Task.objects.values().get(id=task_id)
        # task2.isCompleted = True
        # print(task2.isCompleted)
        return JsonResponse({'status': 'ok', 'task': task2})

    def put(self, request, task_id):
        task3 = Task.objects.get(id=task_id)
        
        print(task3)
        if task3.isCompleted == True:
            task3.isCompleted = False
        
        if task3.isCompleted == False:
            task3.isCompleted = True
        task3.save()
        print("*******task!!!!!!!", task3.isCompleted)
        return JsonResponse({'status': 'ok'})

class usr(View):
    def post(self,request):
        print("Testing!!!!!!!!")
        body = json.loads(request.body.decode())
        print(body, type(body))

        # errors = User.objects.validator(body)
        # if len(errors) > 0:
        #     for key, value in errors.items():
        #         messages.error(request, value)
        #     return JsonResponse({'error': errors})
        # else:
        password1 = body['password']
        print("Passowrd!!!!!!", password1, type(password1))
        pw_hash = bcrypt.hashpw(password1.encode(), bcrypt.gensalt())
        print("********Hashed Password********", pw_hash)
        User.objects.create(username = body['name'], email = body['email'], password = pw_hash)
        print("User created******")
        # print(user1)
        return JsonResponse({'message': 'user successfully created'})


class session(View):
    def post(self, request):
        body = json.loads(request.body.decode())
        print(body, type(body))
        user = User.objects.filter(email = body['email'])
        if user:
            logged_user = user[0]
            current_user = User.objects.get(username=body['name'])
            print("Test123", current_user)
            userinfo = { 'email': current_user.email, 'id': current_user.id }
            print("********", body['password'])
            if bcrypt.checkpw(body['password'].encode(), logged_user.password.encode()):
            # jwt_token = Token.objects.create(user = current_user )
                # token = jwt.encode(userinfo, key, algorithm='HS256').decode('utf-8')
                # print(token)
                # print(type(token))
                # key was set to secret above where you import
                # readableToken = jwt.decode(token, 'secret', algorithms='HS256')
                # print("testing readable token", readableToken)
                return JsonResponse({'message': 'user successfully logged in'})
                # return JsonResponse({'token': token} )

