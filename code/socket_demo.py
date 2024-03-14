import os
import time
import socket
import threading
import requests
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

url = 'http://192.168.0.125/api/users/savedata/'


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
    file_path = os.path.join("../数据文件/脉搏波数据文件", user, path)
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
