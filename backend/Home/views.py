# Home/views.py
 
from django.http import JsonResponse

def home(request):
    data = {
        'hello': 'hello'
    }
    return JsonResponse(data)