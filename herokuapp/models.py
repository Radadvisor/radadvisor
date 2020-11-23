from django.db import models

def db(request):
    greeting=Greeting()
    greeting.save()

    greeting = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
# Create your models here.
