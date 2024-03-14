from django.urls import path

from . import data
from . import sign_in_out
from . import saveData
urlpatterns = [
    path('data/', data.dispatcher),
    path('signin/', sign_in_out.login),
    path('signout/', sign_in_out.logout),
    path('savedata/', saveData.savedata)
]
