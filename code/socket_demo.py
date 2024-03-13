import os
import time
import socket
import threading


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


def build_frame(user, file_name, data):
    return f"{TERMINAL_ID},{user},{file_name},{data}"

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
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((SERVER_ADDRESS, SERVER_PORT))
                    s.sendall(frame.encode('utf8'))
            except Exception as e:
                print(f"Error sending data: {e}")
            time.sleep(1 / SEND_FREQUENCY)  # 控制发送频率

# 控制发送数据的线程


class SendThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.file_names = FILE_NAMES
        self.user = USER
        self._running = threading.Event()

    def run(self):
        self._running.set()
        while self._running.isSet():
            # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            #     s.connect((SERVER_ADDRESS, SERVER_PORT))
            #     s.sendall("hello".encode('utf8'))
            for file_name in self.file_names:
                for user in self.user:
                    send_data(user, file_name)
                    print(f"Sending {file_name} from {user}...")

    def stop(self):
        self._running.clear()

    def resume(self):
        self._running.set()


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
                # print(f"Sending {file_name} from {user}...")


# thread = threading.Thread(target=thread_send, args=(user, file_names))
thread = threading.Thread(target=thread_send, args=())


def restart_thread():
    global restart_flag, thread
    restart_flag = 1
    print(2)
    time.sleep(2.0)
    # if thread.is_alive():
    #     thread.join()
    #     print(1)
    restart_flag = 0
    thread = threading.Thread(target=thread_send, args=())
    thread.start()


if __name__ == "__main__":
    # 创建发送线程
    # send_thread = SendThread()
    # send_thread.start()

    # try:
    #     while True:
    #         command = input("Enter 'start' to start sending data, 'stop' to stop: ")
    #         if command.lower() == 'start':
    #             send_thread.start()
    #         elif command.lower() == 'resume':
    #             send_thread.run()
    #         elif command.lower() == 'stop':
    #             send_thread.stop()
    #         else:
    #             print("Invalid command. Please enter 'start' or 'stop'.")
    # except KeyboardInterrupt:
    #     print("Stopping...")
    #     send_thread.stop()
    #     send_thread.join()
    # thread = threading.Thread(target=thread_send, args=(USER, FILE_NAMES))
    # thread.start()
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
