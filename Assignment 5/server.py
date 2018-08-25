import socket
import ssl

def main():
    KEY = "certificates/server.key"
    CERT = "certificates/server.crt"

    IP = socket.gethostbyname(socket.gethostname())
    PORT = 3001

    print "Server started at " + str(IP) + ":" + str(PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((IP, PORT))
    ssl_sock = ssl.wrap_socket(sock, keyfile=KEY, certfile=CERT, server_side=True)

    ssl_sock.listen(1)
    print "Server is listening...\n"
    (conn, (ip,port)) = ssl_sock.accept()
    print "Connection established with " + str(ip) + ":" + str(port)
    data = conn.recv(1024).decode()
    lst = map(lambda x: int(x), data.split('$'))
    print "Received: " + str(lst)
    print "Returning: " + str(sum(lst))
    conn.send(str(sum(lst)).encode())

    ssl_sock.close()

if __name__ == '__main__':
    main()
