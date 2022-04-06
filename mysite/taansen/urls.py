from django.urls import path
from . import views
from django.views.generic.base import TemplateView

app_name = 'taansen'
urlpatterns = [
    path('home', TemplateView.as_view(template_name='taansen/home.html'),name='home'),   
    path('', views.index, name = 'index'),
    ]
