from django.http import HttpResponse
from common.models import User
from common.models import Data


def printlist(request):
    return HttpResponse('登陆成功')


def get_user(request):
    qs = User.objects.values()

    retstr = ''

    for user in qs:
        for name, value in user.items():
            retstr += f'{name}:{value} | '

        retstr += '<br>'

    return HttpResponse(retstr)


def get_data(request):
    qs = Data.objects.values()

    ph = request.GET.get('user_name', None)

    if ph:
        qs = qs.filter(user_name=ph)

    retstr = ''

    for data in qs:
        for name, value in data.items():
            retstr += f'{name}:{value} | '

        retstr += '<br>'

    return HttpResponse(retstr)
