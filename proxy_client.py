import socket

HOST = "www.google.com"
PORT = 80
BUFFER_SIZE = 4096

pay_load = "GET / HTTP/1.0\r\nHOST: www.google.com\r\n\r\n"

def connect(address):
    try:
        new_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        new_sock.connect(address)
        new_sock.sendall(pay_load.encode())
        new_sock.shutdown(socket.SHUT_WR)
        full_data = new_sock.recv(BUFFER_SIZE)
        print(full_data)
    except Exception as e:
        print(e)
    finally:
        new_sock.close()

def main():
    connect(('127.0.0.1', 8001))
    
if __name__=="__main__":
    main()

        
