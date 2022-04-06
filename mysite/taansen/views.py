# Create your views here.
from email.policy import HTTP
from django.shortcuts import get_object_or_404, render, redirect # !redirect added

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader
from django.core.paginator import Paginator #!
from . models import Song

def index(request): #!
    paginator = Paginator(Song.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "taansen/index.html", {"page_obj":page_obj})