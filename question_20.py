# 파이썬 내장 라이브러리를 이용하여 소켓 서버를 작성하는 코드입니다.
# 이 코드의 에러를 찾아주세요.
# 이 문제는 매우 쉽습니다.

import socket

def start_server(port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', port))
    server_socket.listen()
    print(f"Server is listening on port {port}...")
    
    while True:
        client_socket, addr = server_socket.accept()
		print(f"Connection from {addr} has been established.")
        
        client_socket.send(bytes("Welcome to the server!", "utf-8"))
        
        client_socket.close()

if __name__ == "__main__":
    start_server()