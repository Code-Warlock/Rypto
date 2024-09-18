from django.shortcuts import render

# Create your views here.
from .homepage import data, crypto_offers, gambling_offers

from random import choice


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
        "crumb_title" : "About Ryptocurrencystakes",
        "landing_image" : "assets/images/about_usbg.jpg"
    }
    
    return render(request, "mainapp/about.html",context)
def contact(request):
    context = {
        "content" : data,
        "crumb_title" : "Contact Ryptocurrencystakes",
        "landing_image" : "assets/images/about_usbg.jpg"
    }
    
    return render(request, "mainapp/contact.html",context)

def crypto(request):
    context = {
        "content" : data,
        "offers" : crypto_offers,
        "crumb_title" : "Crypto Offers",
        "landing_image" : "assets/images/about_usbg.jpg"
    }
    
    return render(request, "mainapp/crypto.html",context)

def crypto_offer(request,slug):
    single_offer = next(offer for offer in crypto_offers if offer['tab'] == "1" and offer['slug'] == slug)
    context = {
        "content" : data,
        "offer" : single_offer,
        "crumb_title" : "Crypto Offers",
        "crumb_cat" : single_offer['title'],
        "backlink" : "crypto",
        "landing_image" : "assets/images/about_usbg.jpg"
    }
    
    return render(request, "mainapp/offer.html",context)

def gambling(request):
    context = {
        "content" : data,
        "offers" : gambling_offers,
        "crumb_title" : "Gambling Offers",
        "landing_image" : "assets/images/onlinecasino.jpg"
    }
    
    return render(request, "mainapp/gambling.html",context)

def gambling_offer(request,slug):
    single_offer = next(offer for offer in gambling_offers if offer['tab'] == "2" and offer['slug'] == slug)
    gambling_offer_images = ["assets/images/phonecasino.jpg","assets/images/onlinecasino2.jpg","assets/images/laptopcasino.jpg"]
    context = {
        "content" : data,
        "offer" : single_offer,
        "crumb_title" : "Gambling Offers",
        "crumb_cat" : single_offer['title'],
        "backlink" : "gambling",
        "landing_image" : choice(gambling_offer_images)
        
    }
    
    return render(request, "mainapp/offer.html",context)

def privacy(request):
    context = {
        "content" : data,
        "offers" : gambling_offers,
        "crumb_title" : "PRIVACY POLICY",
        "landing_image" : "assets/images/privacy_policy.jpg",
        "privacy_image" : "assets/images/privacy.jpg",
    }
    
    return render(request, "mainapp/privacy.html",context)

def cookie(request):
    context = {
        "content" : data,
        "offers" : gambling_offers,
        "crumb_title" : "COOKIE POLICY",
        "landing_image" : "assets/images/cookie_policy.png",
        "cookie_image" : "assets/images/cookieimage.jpg",
    }
    
    return render(request, "mainapp/cookie.html",context)