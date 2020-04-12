from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from rest_framework import status, views
from rest_framework.response import Response

from .serializers import UserSerializer

class LoginView(views.APIView):
    def post(self, request):
        # print("Data TesT34!!!!!!!!", request.data.get("password"), request.data.get("email"), type(request.data.get("password")))
        user = authenticate(
            email=request.data.get("email"),
            password=request.data.get("password"),
        )
        # print("!!!!!!!!TEst3#######", user)
        if user is None or not user.is_active:
            return Response({
                'status': 'unauthorized',
                'message': 'password or email is incorrect'
            }, status = status.HTTP_401_UNAUTHORIZED)
        login(request, user)
        return Response(UserSerializer(user).data)

class LogoutView(views.APIView):

    def get(self, request):
        logout(request)
        return Response({}, status=status.HTTP_204_NO_CONTENT)