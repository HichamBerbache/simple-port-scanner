import socket
import sys

ip_address = sys.argv[1]
start_port = int(sys.argv[2])
end_port = int(sys.argv[3]) + 1

for port in range(start_port, end_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(5)
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            print(f'Port {port} is open')
