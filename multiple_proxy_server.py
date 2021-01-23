import socket, sys
from multiprocessing import Process

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def get_ip(host):
    
    try:
        new_ip = socket.gethostbyname(host)
    except socket.gaierror:
        sys.exit()
        
    return new_ip

def handle_req(conn, addr, proxy_end):
    send_full_data = conn.recv(BUFFER_SIZE)
    proxy_end.sendall(send_full_data)
    proxy_end.shutdown(socket.SHUT_WR)

    data = proxy_end.recv(BUFFER_SIZE)
    print("sending data" + data.decode("utf-8"))
    conn.send(data)

def main():

    host = "www.google.com"
    port = 80
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
        proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        proxy_start.bind((HOST, PORT))
        proxy_start.listen(1)
        while True:
            conn, addr = proxy_start.accept()
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
                new_ip = get_ip(host)

                proxy_end.connect((new_ip, port))
                p = Process(target=handle_req, args=(conn, addr, proxy_end))
                p.daemon = True
                p.start()
            conn.close()

if __name__=="__main__":
    main()
