
from django.urls import path
from herokuapp.views import homePageView

urlpatterns = [
    path('', homePageView, name='home')
]
