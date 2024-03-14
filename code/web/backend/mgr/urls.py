from django.urls import path
from . import users
from . import sign_in_out

urlpatterns = [
    path("users/", users.dispatcher),
    path("signin/", sign_in_out.login),
    path("signout/", sign_in_out.logout)
]
