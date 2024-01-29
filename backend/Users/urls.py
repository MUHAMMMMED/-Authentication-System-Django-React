# # users/urls.py
# from django.urls import path
# from .views import CustomUserCreate, CustomAuthToken 

# urlpatterns = [
#     path('signup/', CustomUserCreate.as_view(), name='signup'),
#     path('login/', CustomAuthToken.as_view(), name='login'),
  
# ]


from django.urls import path
from .views import create_user, user_login

urlpatterns = [
    path('create_user/', create_user, name='create_user'),
    path('user_login/', user_login, name='user_login'),
    # Add other URLs as needed
]
