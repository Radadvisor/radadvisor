from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def kontakt(request):
    return render(request, 'kontakt.html')

