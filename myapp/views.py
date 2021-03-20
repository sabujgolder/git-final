from django.shortcuts import render
from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = 'myapp/home.html'
# Create your views here.


class About(TemplateView):
    template_name = 'myapp/about.html'
