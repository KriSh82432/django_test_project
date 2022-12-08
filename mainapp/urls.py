from django.urls import path 
from . import views 

urlpatterns = [ 
    path('home/', views.main, name='main'),
    path('kitchen/', views.index, name='index'),
    path('bath/<name>/<age>', views.show, name='show'),
    path('menu/', views.menu, name='menu'),
    path('query/', views.queryview, name='queryview'),
] 