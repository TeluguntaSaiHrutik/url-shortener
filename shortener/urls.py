from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage_view,name="homepage"),
    path('<str:short_url>',views.redirecter,name="redirect")
]
