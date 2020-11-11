"""
Definition of forms.
"""
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import ContextMixin, TemplateResponseMixin
from django.views.generic.edit import ProcessFormView
from django.db import transaction
from django.db import models
from django.forms import ModelForm

#Import Models
from django.db import models
from django.forms import ModelForm
from .models import ComicInput

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

        
    
    ##############Garage Car Input Forms###############
class ComicInputForm(forms.ModelForm):
    class Meta:
        model = ComicInput
        fields = '__all__'

        #form = ComicInputForm()

        # Creating a form to change an existing article.
        #article = Article.objects.get(pk=1)
        #form = ArticleForm(instance=article)

