"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

from django.forms import ModelForm
from .models import ComicInput
from django.db import models
from django.forms import ModelForm
from .forms import ComicInputForm

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
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
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )


############### Comic Input #####################
def comicinput(request):
     submitted = False
     if request.method == 'POST':
         form = ComicInputForm(request.POST)
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