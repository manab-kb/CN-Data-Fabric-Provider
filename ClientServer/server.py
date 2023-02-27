import socket

host = "127.0.0.1"
port = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as skt:
    skt.bind((host, port))
    skt.listen()
    connect, address = skt.accept()
    with connect:
        print("Connected by " + str(address))
        while True:
            data = connect.recv(1024)
            #if not data:
            #    break
            connect.sendall(data)
