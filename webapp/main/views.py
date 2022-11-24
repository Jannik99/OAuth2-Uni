from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from authlib.integrations.django_client import OAuth
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView, TemplateView

# Create your views here.
def index(request):
    return HttpResponseRedirect(reverse('front'))

class FrontView(TemplateView):
    template_name = 'front.html'

def oauth_authorize(request):
    oauth = OAuth(request)
    redirect_uri = request.build_absolute_uri(reverse('oauth_callback'))
    return oauth.github.authorize_redirect(request, redirect_uri)