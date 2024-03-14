import socket

# 本地服务器地址和端口
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 12345

# 创建TCP套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定地址和端口
server_socket.bind((SERVER_ADDRESS, SERVER_PORT))

# 开始监听连接请求
server_socket.listen(1)
print("等待连接...")

ir_data = [100634, 100628]
red_data = [82355, 82346]


def get_data(data):
    data = data.decode().split(',')
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
    R = ((ir_max + ir_min) * (red_max - red_min)) / ((red_max + red_min) * (ir_max - ir_min))
    SpO2 = (-45.060) * R * R + 30.354 * R + 94.845
    return SpO2


while True:
    # 接受客户端连接
    client_socket, client_address = server_socket.accept()
    print(f"连接来自 {client_address}")

    try:
        # 接收数据
        data = client_socket.recv(1024)
    except Exception as e:
        print("接收数据时出错:", e)
    finally:
        # 关闭客户端套接字
        client_socket.close()

    if data:
        print("血氧饱和度: {:.5f}%".format(get_data(data)))
