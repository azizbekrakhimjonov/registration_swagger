from django.urls import path
from .views import hello_world, register, data_get

urlpatterns = [
    path('hello/', hello_world, name='hello-world'),
    path("register/", register),
    path("data/", data_get),
]