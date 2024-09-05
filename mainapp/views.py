from django.shortcuts import render

# Create your views here.
from .homepage import data


def error_404_view(request, exception):
    return render(request, '404.html')

def index(request):
    
    
    context = {
        "content" : data
    }
    
    return render(request, "mainapp/index.html",context)

def about(request):
    context = {
        "content" : data
    }
    
    return render(request, "mainapp/about2.html",context)