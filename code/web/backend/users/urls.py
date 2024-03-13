from django.urls import path

from . import func

urlpatterns = [
    path('login/', func.printlist),
    path('user/', func.get_user),
    path('data/', func.get_data),
]
