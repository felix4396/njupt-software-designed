from django.http import JsonResponse
import json
from common.models import User


def login(request):
    if request.method == 'POST':
        request.params = json.loads(request.body)
        username = request.params['username']
        password = request.params['password']

        try:
            user = User.objects.get(name=username, user_type=1)
            if user.password == password:
                return JsonResponse({'ret': 0})
            else:
                return JsonResponse({'ret': 1, 'msg': '密码错误'})
        except User.DoesNotExist:
            return JsonResponse({'ret': 1, 'msg': '用户名不存在'})


def logout(request):
    if request.method == 'POST':
        return JsonResponse({'ret': 0})
