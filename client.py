import socket

host = "127.0.0.1"
port = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as skt:
    skt.connect((host, port))
    skt.sendall(b"Hello, world")
    data = skt.recv(1024)
    
print("Received {data}")