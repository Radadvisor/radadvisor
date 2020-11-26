from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def bikes(request):
    return render(request, 'bikes.html')

def wald(request):
    return render(request, 'wald.html')

def bergig(request):
    return render(request, 'bergig.html')

def strasse(request):
    return render(request, 'strasse.html')

def stadt(request):
    return render(request, 'stadt.html')