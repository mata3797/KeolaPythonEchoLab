import socket
import sys

if len(sys.argv) != 3:
    print("Usage: python3 src/httpget.py <IP_ADDRESS> <PORT>")
    sys.exit(1)

theServerAddress = sys.argv[1]
thePath = sys.argv[2]
httpPort = 80

request = (
    f"GET {thePath} HTTP/1.1\r\n"
    f"Host: {theServerAddress}\r\n"
    "Connection: close\r\n"
    "\r\n"
)

print(">|")
print(request, end="")
print("|<")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        # connecting to the server, then send request
        s.connect((theServerAddress, httpPort))
        s.sendall(request.encode("utf-8"))

        response = s.recv(4096)

        print(">|")
        print(response.decode(), end="")
        print("|<")
    except Exception as e:
        print(f"An error occurred: {e}")