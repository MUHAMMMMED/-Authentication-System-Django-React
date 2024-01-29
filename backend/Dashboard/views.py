# Dashboard/views.py
 

from django.http import JsonResponse

def dashboard(request):
    data = {
        'hello': 'hello'
    }
    return JsonResponse(data)