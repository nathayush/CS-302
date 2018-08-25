import socket
import ssl

def main():
    CERT = "certificates/ca.crt"

    server_ip = str(raw_input("Enter server IP: "))
    server_port = int(raw_input("Enter server port: "))

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    ssl_sock = ssl.wrap_socket(sock, ca_certs=CERT, cert_reqs=ssl.CERT_REQUIRED)
    ssl_sock.connect((server_ip, server_port))
    print "\nConnection established with " + str(server_ip) + ":" + str(server_port)

    num1 = raw_input("Enter the first number: ")
    num2 = raw_input("Enter the second number: ")
    ssl_sock.send((num1 + '$' + num2).encode())
    data = ssl_sock.recv(1024).decode()
    print "Sum received from server = " + data

    ssl_sock.close()

if __name__ == '__main__':
    main()
