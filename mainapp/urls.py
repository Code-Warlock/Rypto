from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("crypto/", views.crypto, name="crypto"),
    path("crypto/<slug:slug>/", views.crypto_offer, name="c_offer"),
    path("gambling/", views.gambling, name="gambling"),
    path("gambling/<slug:slug>/", views.gambling_offer, name="offer"),
    path("contact/", views.contact, name="contact"),
    path("privacy-policy/", views.privacy, name="privacy"),
    path("cookie-policy/", views.cookie, name="cookie"),
    path('robots.txt', views.robots_txt, name='robots_txt'),
]
