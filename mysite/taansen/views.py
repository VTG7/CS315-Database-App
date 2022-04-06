# Create your views here.
from email.policy import HTTP
from re import template
from django.shortcuts import get_object_or_404, render, redirect # !redirect added

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator #!
from . models import Song

def index(request): #!
    paginator = Paginator(Song.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "taansen/index.html", {"page_obj":page_obj})

class SignUpView(generic.CreateView):   # For Signup Page
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"
