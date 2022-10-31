from rest_framework import permissions, generics, status, views
from rest_framework.response import Response
from django.contrib.auth import login, logout
from knox.models import AuthToken
from .serializers import RegisterUserSerializer, LoginUserSerializer
from users.models import ExUser

# Create your views here.
        
class RegisterUserView(generics.CreateAPIView):
    
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterUserSerializer
    
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            newUser = serializer.data
            ExUser.objects.create_user(newUser['username'], newUser['email'], newUser['password1'])
            return Response({'success': True})
        else:
            return Response({'success': False, 'errors': serializer.errors})

class LoginUserView(generics.CreateAPIView):
    
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginUserSerializer
    
    def post(self, request):
        serializer = LoginUserSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get('user')
        token =  AuthToken.objects.create(user)[1]
        login(request, user)
        return Response({'success': True, 'token': token, 'email': user.email}, status=status.HTTP_202_ACCEPTED)
    
class LogoutUserView(views.APIView):
    
    permission_classes = [permissions.AllowAny]
    
    def post(self, request, format=None):
        logout(request)
        return Response({'success': True}, status=status.HTTP_202_ACCEPTED)
    