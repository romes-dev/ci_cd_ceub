from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    """
    A simple view that returns a 'Hello, World!' response.
    """
    return HttpResponse("Olá, Mundo do CI/CD!")
# Create your views here.
