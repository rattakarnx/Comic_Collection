"""
Definition of urls for Comic_Collection.
"""

from datetime import datetime
from django.urls import path
from django.urls import path, re_path
from django.contrib import admin
#from django.contrib.auth.views import LoginView, LogoutView
from app import models, forms, views
from django.conf import settings
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('comicinput/', views.comicinput, name='comicinput'),
    path('about/', views.about, name='about'),
    #path('viewer/', views.ComicInventory, name='ComicInventory'),
    url(r'^viewer/$', views.ComicInventory, name ='ComicInventory'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#IMAGES
if settings.DEBUG:
     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'Collector Admin Zone'
admin.site.site_title = 'Collector'