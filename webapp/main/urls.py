from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('front/', views.FrontView.as_view(), name='front'),
    path('oauth/authorize', views.oauth_authorize, name='oauth_authorize'),
    path('oauth/callback', views.oauth_callback, name='oauth_callback'),
]
