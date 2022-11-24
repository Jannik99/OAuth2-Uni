from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('front/', views.FrontView.as_view(), name='front'),

]
