from django.urls import path
from . import users

urlpatterns = [
    path("users/", users.dispatcher),
]
