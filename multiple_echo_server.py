import socket
from multiprocessing import Process

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as new_sock:
        new_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        new_sock.bind((HOST, PORT))
        new_sock.listen(2)
        while True:
            conn,address = new_sock.accept()
            p = Process(target=handle_echo, args=(address, conn))
            p.daemon = True
            p.start()

def handle_echo(address, conn):
    full_data = conn.recv(BUFFER_SIZE)
    conn.sendall(full_data)
    conn.shutdown(socket.SHUT_WR)
    conn.close()

if __name__=='__main__':
    main()
