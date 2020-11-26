from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import BewertungItem


# Create your views here.


def bewertunglist(request):
    all_bewertung_items = BewertungItem.objects.all()
    return render(request, 'bewertung.html',
                  {'all_items': all_bewertung_items})


def addbewertung(request):
    # create a new to do all_itmes
    # save
    # redirect the browser to'/todo/'
    new_item = BewertungItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/bewertung/')


def deletebewertung(request, bewertung_id):
    item_to_delete = BewertungItem.objects.get(id=bewertung_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/bewertung/')
