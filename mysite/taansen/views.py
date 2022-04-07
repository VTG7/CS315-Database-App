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
from . forms import searchForm
from django.db.models import Q

def index(request): #!
    paginator = Paginator(Song.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "taansen/index.html", {"page_obj":page_obj})

class SignUpView(generic.CreateView):   # For Signup Page
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"

def homeView(request):  # For home page, after login
    if request.method == 'POST':
        form = searchForm(request.POST)
        if form.is_valid():
            # will do the query here
            # rn, just putting a dummy link
            song = form.cleaned_data['query']
            #return HttpResponseRedirect('/taansen/accounts/signup')
            object_list = Song.objects.filter(title__contains=song) #! the query to get the songs containing 'song' in their title. Case insensitive matching done
            return render(request, 'taansen/search_results.html',{'object_list':object_list})
    else :
        form = searchForm()

    return render(request, 'taansen/home.html', {'form':form})


