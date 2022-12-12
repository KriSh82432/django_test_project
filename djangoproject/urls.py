from django.contrib import admin 
from django.urls import include, path 

urlpatterns = [ 
    path('', include('mainapp.urls', namespace='mainapp')), 
    path('admin/', admin.site.urls), 
]

handler404 = 'djangoproject.views.handle404'