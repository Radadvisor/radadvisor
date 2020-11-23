
from django.urls import path
from .views import homePageView, AboutPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', homePageView.as_view(), name='home'),
    path('home/', homePageView.as_view(), name='home'),
]
