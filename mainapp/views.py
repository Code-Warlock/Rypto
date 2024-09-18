from django.shortcuts import render

# Create your views here.
from .homepage import data, offers


def error_404_view(request, exception):
    return render(request, '404.html')

def index(request):
    
    
    context = {
        "content" : data
    }
    
    return render(request, "mainapp/index.html",context)

def about(request):
    context = {
        "content" : data,
        "crumb_title" : "About Ryptocurrencystakes"
    }
    
    return render(request, "mainapp/about.html",context)
def contact(request):
    context = {
        "content" : data,
        "crumb_title" : "Contact Ryptocurrencystakes"
    }
    
    return render(request, "mainapp/contact.html",context)

def crypto(request):
    context = {
        "content" : data,
        "offers" : offers,
        "crumb_title" : "Crypto Offers"
    }
    
    return render(request, "mainapp/crypto.html",context)

def crypto_offer(request,slug):
    single_offer = next(offer for offer in offers if offer['tab'] == "1" and offer['slug'] == slug)
    context = {
        "content" : data,
        "offer" : single_offer,
        "crumb_title" : "Crypto Offers",
        "crumb_cat" : single_offer['title'],
        "backlink" : "crypto"
    }
    
    return render(request, "mainapp/offer.html",context)

def gambling(request):
    context = {
        "content" : data,
        "offers" : offers,
        "crumb_title" : "Gambling Offers"
    }
    
    return render(request, "mainapp/gambling.html",context)

def gambling_offer(request,slug):
    single_offer = next(offer for offer in offers if offer['tab'] == "2" and offer['slug'] == slug)
    context = {
        "content" : data,
        "offer" : single_offer,
        "crumb_title" : "Gambling Offers",
        "crumb_cat" : single_offer['title'],
        "backlink" : "gambling"
    }
    
    return render(request, "mainapp/offer.html",context)