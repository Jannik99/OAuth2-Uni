from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from authlib.integrations.django_client import OAuth
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView, TemplateView

from webapp import settings

# OAuth setup
oauth = OAuth() # Create new OAUth object
oauth.register(settings.OAUTH_CLIENT_NAME, **settings.OAUTH_CLIENT) # Register new oauth client with given settings


# Create your views here.
def index(request):
    return HttpResponseRedirect(reverse('front'))


class FrontView(TemplateView):
    template_name = 'front.html'


def oauth_authorize(request):
    github = oauth.create_client(settings.OAUTH_CLIENT_NAME) # Create new client with given name. This is a name we registered in the oauth object
    redirect_uri = 'http://127.0.0.1:8000/oauth/callback'
    return github.authorize_redirect(request, redirect_uri) # Just a redirect to the chosen Auth Provider


def oauth_callback(request):
    token = oauth.github.authorize_access_token(request) # Get the token from the request
    resp = oauth.github.get('user', token=token) # Get the response
    resp.raise_for_status() # Raise an error if the response is not 200
    profile = resp.json() # Get the json from the response which is the user info
    context = {
        'profile': profile, # Pass the profile to the context
        'token': token # Pass the token to the context
    }
    return render(request, "result.html", context)
