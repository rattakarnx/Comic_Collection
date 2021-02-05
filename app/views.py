"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.forms import ModelForm
from .models import ComicInput
from django.db import models
from app import forms
from import_export import resources
from .forms import TitleChoiceField
from .forms import NotesChoiceField
from .forms import PublisherChoiceField
from .forms import ComicInputForm
from .forms import editform
from django.db.models import Avg, Max, Min, Sum
from django.db.models import Q
from django.contrib import messages

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Kollector',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'How to use the Kollector App',
            'year':datetime.now().year,
        }
    )


############### Comic Input #####################
def comicinput(request):
     submitted = False
     if request.method == 'POST':
         form = ComicInputForm(request.POST, request.FILES)
         if form.is_valid():
             form.save()
             return HttpResponseRedirect('/comicinput/?submitted=True')
     else:
         form = ComicInputForm()
         if 'submitted' in request.GET:
             submitted = True
     return render(request, 
         'comicinput.html', 
         {'form': form, 'submitted': submitted})

 ###################### Collection Viewer #############
def ComicInventory(request):

    title_list = TitleChoiceField()
    publisher_list = PublisherChoiceField()
    sellingnotes_list = NotesChoiceField()

    if request.GET.get('titles'):
        selected_title = request.GET.get('titles')
        displayInventory=ComicInput.objects.filter(Title=selected_title)
        DisplaySumValue=ComicInput.objects.all().filter(Title=selected_title).aggregate(Sum('Value'))
    elif request.GET.get('sellingnotes'):
        selected_notes = request.GET.get('sellingnotes')
        displayInventory=ComicInput.objects.filter(SellingNotes=selected_notes)
        DisplaySumValue=ComicInput.objects.all().filter(SellingNotes=selected_notes).aggregate(Sum('Value'))
    elif request.GET.get('publisher'):
        selected_publisher = request.GET.get('publisher')
        displayInventory=ComicInput.objects.filter(Publisher=selected_publisher)
        DisplaySumValue=ComicInput.objects.all().filter(Publisher=selected_publisher).aggregate(Sum('Value'))
    else:
        displayInventory=ComicInput.objects.all()
        DisplaySumValue=ComicInput.objects.all().aggregate(Sum('Value'))
    context = {
        'displayInventory': displayInventory,
        'DisplaySumValue': DisplaySumValue,
        'title_list': title_list,
        'sellingnotes_list': sellingnotes_list,
        'publisher_list': publisher_list,
        #EDIT  context????? 12 min

 	}

    return render(request, 'app/viewer.html',context)


def edit(request, id):
   record = ComicInput.objects.get(pk = id)
   #you can do this for as many fields as you like
   #here I asume you had a form with input like <input type="text" name="name"/>
   #so it's basically like that for all form fields
   #iss.Publisher = request.POST.get('Publisher')
   #iss.save()
   #return HttpResponse('updated')
   
   return render(request, 'app/edit.html',{"ComicInput":record})

def update(request, id):
   updaterecord = ComicInput.objects.get(id = id)
   form = editform(request.POST, request.FILES)
   if form.is_valid():
    form.save()
    messages.success(request,"``*BOOM*`` - your comic was updated")
    return render(request, 'app/edit.html',{"ComicInput":updaterecord})
   else :
            return render(request, 'app/edit.html', {"ComicInput":updaterecord})

def delete(request, id):
   iss = ComiCInputs.objects.get(id = id)
   iss.delete()
   return HttpResponse('deleted')