import requests
import json

# 定义目标URL和要发送的数据
url = 'http://192.168.0.125/api/users/savedata/'
register_data = {
    'action': 'add_user',
    'data': {
        'name': 'shiro',
        'password': '123456',
        'user_type': '1'
    }
}
login_data = {
    'username': 'shiro',
    'password': '123456'
}
send_data = {
    "TERMINAL_ID": "414585",
    "user": "采样者1",
    "file_name": "跑步",
    "data": "100634,82355"
}
# 发送POST请求
response = requests.post(url, data=json.dumps(send_data))

# 检查响应状态码
if response.status_code == 200:
    print('请求成功！')
    print('响应内容：', response.text)
else:
    print('请求失败：', response.status_code)
