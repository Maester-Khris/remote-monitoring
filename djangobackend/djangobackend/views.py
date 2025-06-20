from django.shortcuts import render
from django.http import HttpResponse # Import HttpResponse
from django.http import HttpResponse
from rest_framework import status

# Create your views here.
def index(request):
    return render(request, "index.html",{})

def about(request):
    return render(request, "about.html",{})

def health_check_view(request):
    """
    A simple health check endpoint for Kubernetes probes.
    """
    try:
        return HttpResponse('OK', status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return HttpResponse({'response': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    