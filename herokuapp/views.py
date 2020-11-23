from django.views.generic import TemplateView


# Standart http Response nur zum Test
# from django.http import HttpResponse

# Standart als Test
# def homePageView(request):´
#    return HttpResponse('Willkommen beim Radadvisor!')
# Create your views here.

class homePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'
