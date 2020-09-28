from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from .models import Pic
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = "pages/about.html"

class ContactPageView(TemplateView):
    template_name = "pages/contact.html"

class ThankYouView(TemplateView):
    template_name = "pages/thankyou.html"

class PhotosView(ListView):
    model = Pic
    template_name = 'pages/photos.html'
