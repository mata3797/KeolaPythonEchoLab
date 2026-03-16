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