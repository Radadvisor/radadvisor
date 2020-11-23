from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('Willkommen beim Radadvisor!')
# Create your views here.
