 
    

# # users/views.py
# from django.http import JsonResponse
# from rest_framework import generics, permissions
# from rest_framework.response import Response
# from rest_framework.authtoken.models import Token
# from rest_framework.authtoken.views import ObtainAuthToken
# from .models import CustomUser
# from .serializers import CustomUserSerializer
# from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated

# class CustomUserCreate(generics.CreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer
#     permission_classes = [permissions.AllowAny]




# # user = User.objects.create_user(
# #     username="your_username",
# #     email="your_email@example.com",
# #     password="your_password",
# #     is_staff=True,
# #     is_superuser=True,
# # )
# # user.save()












# @api_view(['POST'])
# @permission_classes([AllowAny])
# def user_login(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
#     user = authenticate(request, username=username, password=password)
#     if user:
#         login(request, user)
#         return Response(CustomUserSerializer(user).data, status=status.HTTP_200_OK)
#     return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# @api_view(['POST'])
# @permission_classes([AllowAny])
# class user_login(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         response = super().post(request, *args, **kwargs)
#         token = Token.objects.get(key=response.data['token'])
#         user = token.user  # Access the associated CustomUser object

#         print('user_id,', token.user_id)
#         print('user_type,', user.user_type)
#         print('user ,', user )
#         context={
#             'token': token.key,
#                 'username': user.username,  # Include any other relevant fields
#             'user_id': token.user_id,
#             'user_type': user.user_type,
            
#               }
#         return Response(context)

 
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny
# from .serializers import CustomUserSerializer
# from django.contrib.auth import authenticate, login

# @api_view(['POST'])
# @permission_classes([AllowAny])
# def create_user(request):
#     serializer = CustomUserSerializer(data=request.data)
#     if serializer.is_valid():
#         user = serializer.save()
#         return Response(CustomUserSerializer(user).data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from .serializers import CustomUserSerializer

 

@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    # Debugging: Print the received credentials
    print(f'Login attempt - Username: {username}, Password: {password}')

    user = authenticate(request, username=username, password=password)

    # Debugging: Print the authenticated user
    print('Authenticated user:', user)

    if user:
        login(request, user)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username,
            'user_id': user.id,
            'user_type': user.user_type,
        }, status=status.HTTP_200_OK)
    return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from .serializers import CustomUserSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username,
            'user_id': user.id,
            'user_type': user.user_type,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
