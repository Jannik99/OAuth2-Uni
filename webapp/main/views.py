from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from authlib.integrations.django_client import OAuth
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView, TemplateView

from webapp import settings

# OAuth setup
oauth = OAuth()
oauth.register(settings.OAUTH_CLIENT_NAME, **settings.OAUTH_CLIENT)


# Create your views here.
def index(request):
    return HttpResponseRedirect(reverse('front'))


class FrontView(TemplateView):
    template_name = 'front.html'


def oauth_authorize(request):
    github = oauth.create_client(settings.OAUTH_CLIENT_NAME)
    redirect_uri = 'http://127.0.0.1:8000/oauth/callback'
    return github.authorize_redirect(request, redirect_uri)


def oauth_callback(request):
    token = oauth.github.authorize_access_token(request)
    resp = oauth.github.get('user', token=token)
    resp.raise_for_status()
    profile = resp.json()
    context = {
        'profile': profile,
        'token': token
    }
    print(context)
    return render(request, "result.html", context)
