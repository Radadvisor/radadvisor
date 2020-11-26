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

def wald(request):
    return render(request, 'wald.html')

def bergig(request):
    return render(request, 'bergig.html')

def strasse(request):
    return render(request, 'strasse.html')

def stadt(request):
    return render(request, 'stadt.html')

def electric(request):
    return render(request, 'electric.html')

def ebike(request):
    return render(request, 'ebike.html')

def waldsportlich(request):
    return render(request, 'waldsportlich.html')

def waldnormal(request):
    return render(request, 'waldnormal.html')

def strassesportlich(request):
    return render(request, 'strassesportlich.html')

def strassenormal(request):
    return render(request, 'strassenormal.html')

def stadtfalten(request):
    return render(request, 'stadtfalt.html')

def stadtnormal(request):
    return render(request, 'stadtnormal.html')

def bergsprung(request):
    return render(request, 'bergigsprung.html')

def bergnormal(request):
    return render(request, 'bergignormal.html')