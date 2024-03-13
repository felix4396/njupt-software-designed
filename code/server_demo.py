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

while True:
    # 接受客户端连接
    client_socket, client_address = server_socket.accept()
    print(f"连接来自 {client_address}")

    try:
        # 接收数据
        data = client_socket.recv(1024)
        if data:
            print("接收到的数据:", data.decode())
    except Exception as e:
        print("接收数据时出错:", e)
    finally:
        # 关闭客户端套接字
        client_socket.close()
