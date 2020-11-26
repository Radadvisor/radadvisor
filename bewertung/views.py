from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Bewertung
# Create your views here.


def bewertunglist(request):
    all_bewertungen_items = Bewertung.objects.all()
    return render(request, 'bewertung.html',
                  {'all_items': all_bewertungen_items})

def addbewertung(request):
    #create a new to do all_itmes
    #save
    #redirect the browser to'/todo/'
    new_item = Bewertung(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/bewertung/')

def deletebewertung(request, bewertung_id):
    item_to_delete = Bewertung.objects.get(id=bewertung_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/bewertung/')