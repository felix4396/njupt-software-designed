from common.models import Data, Terminal
from django.http import JsonResponse
import json
from django.utils import timezone

ir_data = [100634, 100628]
red_data = [82355, 82346]


def get_oxygen(data):
    data = data.split(',')
    if len(ir_data) > 10:
        ir_data.pop(0)
        red_data.pop(0)
    ir_data.append(int(data[-2]))
    red_data.append(int(data[-1]))
    # print(ir_data, red_data)

    ir_max = max(ir_data)
    ir_min = min(ir_data)
    red_max = max(red_data)
    red_min = min(red_data)
    r = ((ir_max + ir_min) * (red_max - red_min)) / ((red_max + red_min) * (ir_max - ir_min))
    result = (-45.060) * r * r + 30.354 * r + 94.845
    return "{:.5f}".format(result)
    # return 0

def savedata(request):
    if request.method == 'POST':
        request.params = json.loads(request.body)
    else:
        return JsonResponse({'ret': 1})
    terminal_id = request.params['TERMINAL_ID']
    username = request.params['user']
    activity = request.params['file_name']
    data = request.params['data']
    oxygen = get_oxygen(data)

    record = Data.objects.create(
        user_name=username,
        blood_oxygen=oxygen,
        time_stamp=timezone.localtime(),  # d1.strftime("%Y-%m-%d %H:%M:%S")
        terminal_id=terminal_id,
        activity=activity
    )

    return JsonResponse({'ret': 0})
