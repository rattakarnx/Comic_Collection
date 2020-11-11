"""
Definition of models.
"""

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models


# Create your models here.


class ComicInput(models.Model):
        Publisher = models.CharField(max_length=50, default='Marvel',blank=False)
        Title = models.CharField(max_length=30,default='')
        Number = models.IntegerField(default='', blank=True)
        Grade = models.CharField(max_length=30, default='', blank=False)
        Cost = models.DecimalField(max_digits=10, decimal_places=2, default='1.95')
        Value = models.DecimalField(max_digits=10, decimal_places=2, default='1.95')
        StoryLine = models.CharField(max_length=25, default='', blank=True)
        SellingNotes = models.CharField(max_length=50, default='',blank=False)
        CoverPic = models.ImageField(upload_to='Comic_Pics', default=False,blank=True)
        BackPic = models.ImageField(upload_to='Comic_Pics', default=False,blank=True)
        ContentPic = models.ImageField(upload_to='Comic_Pics', default=False,blank=True)
        

        def __str__(self):
            return '%s %s' % (self.Title, self.Grade)

        class Meta:
            ordering = ('Title',)