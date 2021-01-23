import socket, time

host = ""
port = 8001
buffer_size = 1024

def main():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((host, port))
        sock.listen(2)
        while True:
            conn, addr = sock.accept()
            print('connected by', addr)
            data = conn.recv(buffer_size)
            time.sleep(0.5)
            conn.sendall(data)
            conn.close()
            

if __name__=="__main__":
    main()
