from django.urls import path
from .views import hello_world, register_user, get_items, delete_items

urlpatterns = [
    path('hello/', hello_world),
    path("register/", register_user),
    path("data/", get_items),
    path("delete/<int:pk>/", delete_items),
]