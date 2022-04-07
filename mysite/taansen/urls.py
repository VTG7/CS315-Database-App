from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from .views import SignUpView

app_name = 'taansen'
urlpatterns = [
    path('signup', SignUpView.as_view(), name='signup'),
    path('home', views.homeView, name='home'),   
    path('', views.index, name = 'index'),
    ]
