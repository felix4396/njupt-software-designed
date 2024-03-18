import os
import time
import threading
import requests
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


FILE_NAMES = ["静坐采样数据", "跑步", "上楼运动后采样数据"]
file_names = ["静坐采样数据", "跑步", "上楼运动后采样数据"]
USER = ["采样者1", "采样者2", "采样者3"]
users = ["采样者1", "采样者2", "采样者3"]
SEND_FREQUENCY = 1
TERMINAL_ID = "TERMINAL_1"
flag = 0
restart_flag = 0
# 本地服务器地址和端口
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 12345

url = 'http://8.136.115.253/api/users/savedata/'


# def build_frame(user, file_name, data):
#     return f"{TERMINAL_ID},{user},{file_name},{data}"


def build_frame(user, file_name, data):
    retlist = {
        "TERMINAL_ID": TERMINAL_ID,
        "user": user,
        "file_name": file_name,
        "data": data
    }
    return retlist
    # 读取数据并发送


def send_data(user, file_name):

    path = file_name+".txt"
    file_path = os.path.join("..\\数据文件\\脉搏波数据文件", user, path)
    print(file_path)
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines[1:]:  # 跳过第一行标签
            # 线程重启标志
            if restart_flag:
                break
            # 线程启动标志
            while not flag and not restart_flag:
                pass

            data = line.strip().split('   ')
            frame = build_frame(user, file_name, ','.join(data))
            try:
                response = requests.post(url, data=json.dumps(frame))
                if response.status_code == 200:
                    print('请求成功！')
                    print('响应内容：', response.text)
                else:
                    print('请求失败：', response.status_code)
            except Exception as e:
                print(f"Error sending data: {e}")
            time.sleep(1 / SEND_FREQUENCY)  # 控制发送频率


class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        global flag
        # 设置响应状态码为200
        self.send_response(200)
        # 设置响应头部信息
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        # 读取请求正文
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # 解析 JSON 数据
        try:
            json_data = json.loads(post_data.decode('utf-8'))
            flag = json_data['status']
            if flag == 'start':
                flag = 1
            elif flag == 'stop':
                flag = 0

            # 构造响应数据
            response_data = {'ret': '0', 'msg': 'success'}
            response = json.dumps(response_data)
            # 发送响应数据
            self.wfile.write(response.encode('utf-8'))
        except json.JSONDecodeError:
            # 如果无法解析 JSON 数据，返回错误信息
            response_data = {'ret': '1'}
            response = json.dumps(response_data)
            self.wfile.write(response.encode('utf-8'))


def run_server(port=12345):
    # 指定服务器地址和端口
    server_address = ('127.0.0.1', port)
    # 创建 HTTP 服务器
    httpd = HTTPServer(server_address, MyHTTPRequestHandler)
    # 开始监听客户端请求
    print(f"Server running on port {port}...")
    httpd.serve_forever()


def thread_send():
    global restart_flag, flag, file_names, users
    while True:
        # 线程重启标志
        if restart_flag:
            break
        # 线程启动标志
        while not flag and not restart_flag:
            pass

        for file_name in file_names:
            # 线程重启标志
            if restart_flag:
                break

            for user in users:
                # 线程重启标志
                if restart_flag:
                    break

                send_data(user, file_name)


thread = threading.Thread(target=thread_send, args=())
thread_get = threading.Thread(target=run_server, args=())


def restart_thread():
    global restart_flag, thread
    restart_flag = 1
    print(2)
    time.sleep(2.0)
    restart_flag = 0
    thread = threading.Thread(target=thread_send, args=())
    thread.start()


if __name__ == "__main__":

    restart_thread()
    try:
        while True:
            command = input("Enter 'start' to start sending data, 'stop' to stop: ")
            if command.lower() == 'start':
                flag = 1
            elif command.lower() == 'stop':
                flag = 0
            elif command.lower() == 'restart':
                # restart_flag = 1
                # thread.join()
                # restart_flag = 0
                restart_thread()

            else:
                print("Invalid command. Please enter 'start' or 'stop'.")
    except KeyboardInterrupt:
        print("Stopping...")
        # thread.join()
