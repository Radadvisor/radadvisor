#config für alle Apps
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls)
    path('', include('herokuapp.urls'))
]