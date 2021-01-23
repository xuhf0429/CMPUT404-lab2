import socket

host = "www.google.com"
port = 80
buffer_size = 1024
new_req = 'GET / HTTP/1.0\r\nHost:{}\r\n\r\n'.format(host)

new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = socket.gethostbyname(host)
new_socket.connect((ip, port))
new_socket.sendall(new_req.encode())
new_socket.shutdown(socket.SHUT_WR)

full_data = b""
while True:
    data = new_socket.recv(buffer_size)
    if not data:
        break
    full_data += data
print(full_data)


    
    
