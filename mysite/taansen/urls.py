from django.urls import path
from . import views

app_name = 'taansen'
urlpatterns = [
    path('', views.index, name = 'index')   
    ]
