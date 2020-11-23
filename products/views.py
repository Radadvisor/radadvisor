from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def products(request):
    return render(request, 'products.html')