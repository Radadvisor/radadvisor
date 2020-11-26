#config für alle Apps
from django.contrib import admin
from django.urls import path
from home.views import homepage
from kontakt.views import kontakt
from bewertung.views import bewertunglist, addbewertung, deletebewertung
from bikes.views import bikes, wald, strasse, bergig, stadt, electric, ebike, waldsportlich, waldnormal, strassenormal, strassesportlich, stadtfalten, stadtnormal, bergnormal, bergsprung



urlpatterns = [
    path('', homepage),
    path('home/', homepage),
    path('bikes/', homepage),
    path('admin/', admin.site.urls),
    path('noelectric/bikes/', bikes),
    path('noelectric/bikes/wald/', wald),
    path('noelectric/bikes/wald/sportlich/', waldsportlich),
    path('noelectric/bikes/wald/normal/', waldnormal),
    path('noelectric/bikes/strasse/', strasse),
    path('noelectric/bikes/strasse/sportlich/', strassesportlich),
    path('noelectric/bikes/strasse/normal/', strassenormal),
    path('noelectric/bikes/stadt/', stadt),
    path('noelectric/bikes/stadt/falten/', stadtfalten),
    path('noelectric/bikes/stadt/normal/', stadtnormal),
    path('noelectric/bikes/bergig/', bergig),
    path('noelectric/bikes/bergig/sprung/', bergsprung),
    path('noelectric/bikes/bergig/normal/', bergnormal),
    path('electric/', electric),
    path('kontakt/', kontakt),
    path('electric/ebike/', ebike),
    path('bewertung/', bewertunglist),
    path('addbewertung/', addbewertung),
    path('deletebewertung/<int:bewertung_id>/', deletebewertung),
]