from django.contrib import admin
from django.urls import path
from log import views


urlpatterns = [
    path("", views.my_view, name="home")
]