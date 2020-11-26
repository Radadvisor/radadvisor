#config für alle Apps
from django.contrib import admin
from django.urls import path
from home.views import homepage
from kontakt.views import kontakt
from bewertung.views import bewertunglist, addbewertung, deletebewertung
from bikes.views import bikes, wald, strasse, stadt, bergig


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', homepage),
    path('', homepage),
    path('kontakt/', kontakt),
    path('bikes/', bikes),
    path('bikes/wald/', wald),
    path('bikes/strasse/', strasse),
    path('bikes/stadt/', stadt),
    path('bikes/bergig/', bergig),
    path('bewertung/', bewertunglist),
    path('addbewertung/', addbewertung),
    path('deletebewertung/<int:bewertung_id>/', deletebewertung)
]