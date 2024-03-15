from django.http import JsonResponse
import json
from common.models import User, Data


def get_data(request):
    username = request.params['user_name']

    qs = Data.objects.values()

    qs = qs.filter(user_name=username)
    if qs:
        retlist = list(qs)
        if len(retlist) > 11:
            retlist = retlist[-11:]
        return JsonResponse({'ret': 0, 'retlist': retlist})
    else:
        return JsonResponse({'ret': 1, 'msg': f'username 为`{username}`的用户不存在'})


def clean_data(request):
    username = request.params['user_name']
    try:
        data = Data.objects.get(user_name=username)
    except Data.DoesNotExist:
        return JsonResponse({'ret': 0, 'msg': f'用户名为`{username}`的用户数据不存在'})

    data.delete()
    return JsonResponse({'ret': 0})


def control(request):
    status = request.params['status']

    return JsonResponse({'ret': 0, 'msg': f'模拟端已{status}'})


def dispatcher(request):
    if request.method == 'GET':
        request.params = request.GET
    elif request.method == 'POST' or 'PUT' or 'DELETE':
        request.params = json.loads(request.body)

    action = request.params['action']
    if action == 'get_data':
        return get_data(request)
    elif action == 'control':
        return control(request)
    elif action == 'clean_data':
        return clean_data(request)
