#config für alle Apps
from django.contrib import admin
from django.urls import path
from home.views import homepage
from todo.views import todolist, addTodo, deleteTodo
from bikes.views import bikes, wald, strasse, stadt, bergig


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', homepage),
    path('', homepage),
    path('bikes/', bikes),
    path('bikes/wald/', wald),
    path('bikes/strasse/', strasse),
    path('bikes/stadt/', stadt),
    path('bikes/bergig/', bergig),
    path('todo/', todolist),
    path('addTodo/', addTodo),
    path('deleteTodo/<int:todo_id>/', deleteTodo)
]