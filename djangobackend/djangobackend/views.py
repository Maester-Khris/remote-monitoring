from django.shortcuts import render
from django.http import HttpResponse # Import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html",{})

def about(request):
    return render(request, "about.html",{})

def health_check_view(request):
    """
    A simple health check endpoint for Kubernetes probes.
    """
    return HttpResponse("OK", status=200)