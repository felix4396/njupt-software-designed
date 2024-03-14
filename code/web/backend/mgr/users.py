from django.http import JsonResponse
import json
from common.models import User, Data


def list_user(request):
    qs = User.objects.values()
    retlist = list(qs)
    return JsonResponse({'ret': 0, 'retlist': retlist})


def add_user(request):
    info = request.params['data']
    try:
        record = User.objects.create(
            name=info['name'],
            password=info['password'],
            user_type=info['user_type']
        )
        return JsonResponse({'ret': 0, 'id': record.id})
    except Exception as e:
        return JsonResponse({"ret": 1, "msg": Exception})


def modify_user(request):
    username = request.params['user_name']
    new_password = request.params['password']

    try:
        user = User.objects.get(user_name=username)
    except User.DoesNotExist:
        return JsonResponse({'ret': 1, 'msg': f'username 为`{username}`的客户不存在'})

    user.password = new_password
    user.save()

    return JsonResponse({'ret': 0})


def delete_user(requests):
    username = requests.params['user_name']

    try:
        user = User.objects.get(user_name=username)

    except User.DoesNotExist:
        return JsonResponse({'ret': 1, 'msg': f'username 为`{username}`的客户不存在'})

    user.delete()

    return JsonResponse({'ret': 0})


def get_data(request):
    username = request.params['user_name']

    qs = Data.objects.values()

    qs = qs.filter(user_name=username)
    if qs:
        retlist = list(qs)
        return JsonResponse({'ret': 0, 'retlist': retlist})
    else:
        return JsonResponse({'ret': 1, 'msg': f'username 为`{username}`的用户不存在'})


def dispatcher(request):
    # 将请求参数统一放入request 的 params 属性中，方便后续处理

    # GET请求 参数在url中，同过request 对象的 GET属性获取
    if request.method == 'GET':
        request.params = request.GET

    # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
    elif request.method in ['POST', 'PUT', 'DELETE']:
        # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
        request.params = json.loads(request.body)

    # 根据不同的action分派给不同的函数进行处理
    action = request.params['action']
    if action == 'list_user':
        return list_user(request)
    elif action == 'add_user':
        return add_user(request)
    elif action == 'modify_user':
        return modify_user(request)
    elif action == 'del_user':
        return delete_user(request)
    elif action == 'get_data':
        return get_data(request)

    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})
