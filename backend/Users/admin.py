 

# Register your models here.
from django.contrib import admin
from .models import CustomUser 

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_type')
    # Add other configurations as needed
