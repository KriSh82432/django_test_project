from django.urls import path 
from . import views 
from django.views.generic import TemplateView

app_name = "mainapp"

urlpatterns = [ 
    path('home/', views.main, name='main'),
    path('kitchen/', views.index, name='index'),
    path('bath/<name>/<age>', views.show, name='show'),
    path('menu/', TemplateView.as_view(template_name = '../templates/index.html')),
    path('query/', views.queryview, name='queryview'),
]