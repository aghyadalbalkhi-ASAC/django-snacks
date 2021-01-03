from django.contrib import admin
from django.urls import path , include
from .views import HomeView,about

urlpatterns = [
    path('',HomeView.as_view(),name='Home'),
    path('about/',about.as_view(),name='about'),

]
