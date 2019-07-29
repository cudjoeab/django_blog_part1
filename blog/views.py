from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render
from blog.models import Article 

def root(request):
    return HttpResponseRedirect('/home')

def home_page(request):
    # context = {}

    context = { 
    'articles': Article.objects.all(),
    'current_time': datetime.now() 
    }
    response = render(request, 'index.html', context)
    return HttpResponse(response)

