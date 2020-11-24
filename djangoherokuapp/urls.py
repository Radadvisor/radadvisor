#config für alle Apps
from django.contrib import admin
from django.urls import path
from home.views import homepage
from products.views import products


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', homepage),
    path('', homepage),
    path('products/', products),
]