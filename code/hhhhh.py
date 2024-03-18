from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
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
                print(1)
            elif flag == 'stop':
                print(2)

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


if __name__ == '__main__':
    run_server()
