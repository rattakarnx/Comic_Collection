"""
Definition of models.
"""

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.utils import timezone
import datetime


#Choices
Edition_Choices = [
    ('Stnd', 'Stnd'),
    ('Dlx', 'Dlx'),
    ('Nws', 'Nws'),
    ('Var', 'Var'),
    ('Sgn','Sgn'),
    ('Rpt','Rpt'),
    ('UK','UK'),
    ('CAD','CAD'),
]

Publisher_Choices = [
    ( 'Atlas', 'Atlas'),
    ( 'Boom', 'Boom'),
    ( 'Caliber', 'Caliber'),
    ( 'Charlton', 'Charlton'),
    ( 'Dargaurd', 'Dargaurd'),
    ( 'Delcourt', 'Delcourt'),
    ( 'Dupuis', 'Dupuis'),
    ( 'DC', 'DC'),
    ( 'DC Vertigo', 'DC Vertigo'),
    ( 'Dark Horse', 'Dark Horse'),
    ( 'Dynamite', 'Dynamite'),
    ( 'EC', 'EC'),
    ( 'Epic', 'Epic'),
    ( 'Fantagraphics', 'Fantagraphics'),
    ( 'IDW', 'IDW'),
    ( 'Image', 'Image'),
    ( 'Kodansha', 'Kodansha'),
    ( 'Malibu', 'Malibu'),
    ( 'Marvel', 'Marvel'),
    ( 'Mirage', 'Mirage'),
    ( 'Rebillion', 'Rebillion'),
    ('Shueisha','Shueisha'),
    ( 'Shogakukan', 'Shogakukan'),
    ( 'Soleil', 'Soleil'),
    ( 'Other', 'Other'),

]


Series_Choices = [
    ('1st', '1st'),
    ('2nd', '2nd'),
    ('3rd', '3rd'),
    ('4th', '4th'),
    ('5th', '5th'),
    ('6th', '6th'),
    ('7th', '7th'),
]

Type_Choices = [
    ('Reg', 'Reg'),
    ('Ann', 'Ann'),
    ('Spc', 'Spc'),
]

Grade_Choices = [
    ('MT', 'MT'),
    ('NM', 'NM+'),
    ('NM', 'NM'),
    ('NM-', 'NM-'),
    ('NM/VF', 'NM/VF'),
    ('VF+', 'VF+'),
    ('VF', 'VF'),
    ('VF-', 'VF-'),
    ('VF/FN', 'VF/FN'),
    ('FN+', 'FN+'),
    ('FN', 'FN'),
    ('FN-', 'FN-'),
    ('FN/VG', 'FN/VG'),
    ('VG', 'VG'),
    ('VG/GD', 'VG/GD'),
    ('GD', 'GD'),
    ('FR', 'FR'),
    ('PR', 'PR'),
]

Grade_Body_Choices = [
    ('CGS', 'CGS'),
    ('CBCS', 'CBCS'),
    ('PGX', 'PGX'),
    ('EGS', 'EGS'),
]

Month_Choices = [
    ('Jan', 'Jan'),
    ('Feb', 'Feb'),
    ('Mar', 'Mar'),
    ('Apr', 'Apr'),
]

year_dropdown = []
for y in range(1940, (datetime.datetime.now().year + 1)):
    year_dropdown.append((y, y))

# Create your models here.


class ComicInput(models.Model):
        Publisher = models.CharField(max_length=20, default='Marvel',choices = Publisher_Choices)
        Title = models.CharField(max_length=50,default='')
        Series = models.CharField(max_length=8,default='1st', choices=Series_Choices)
        Type = models.CharField(max_length=30,default='Reg', choices=Type_Choices)
        Number = models.IntegerField(default='', blank=False)
        Edition = models.CharField(max_length=8,choices=Edition_Choices, default='Std')
        Grade = models.CharField(max_length=5, default='NM/VF', choices=Grade_Choices)
        Cost = models.DecimalField(max_digits=10, decimal_places=2, default='1.95')
        Value = models.DecimalField(max_digits=10, decimal_places=2, default='1.95')
        SoldAmt = models.DecimalField(max_digits=10, decimal_places=2, default='0.00')
        StoryLine = models.CharField(max_length=300, default='', blank=True, null=True)
        SellingNotes = models.CharField(max_length=300, default='',blank=True, null=True)
        CoverPic = models.ImageField(upload_to='Comic_Pics', default='Comic_Pics/default.png',blank=True)
        BackPic = models.ImageField(upload_to='Comic_Pics', default='Comic_Pics/default.png',blank=True)
        ContentPic = models.ImageField(upload_to='Comic_Pics', default='Comic_Pics/default.png',blank=True)
        year = models.IntegerField(default='', null=True, blank=True)
        GradeBody = models.CharField(max_length=8, choices=Grade_Body_Choices, default='', null=True, blank=True)
        GradeCode= models.CharField(max_length=12, blank=True, null=True)
        

        def __str__(self):
            return '%s %s %s' % (self.Title, self.Number, self.Grade)

        class Meta:
            ordering = ('Title', 'Series', 'Number')






class ComicVineApi(models.Model):
        Publisher = models.CharField(max_length=50, default='')
        Title= models.CharField(max_length=100,default='')
        Series = models.CharField(max_length=8,default='1st')
        Number= models.IntegerField(default='', blank=False)