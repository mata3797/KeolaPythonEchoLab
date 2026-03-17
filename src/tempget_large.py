import socket
import sys
import time

if len(sys.argv) < 3:
    print("Usage: python3 src/httpget.py <IP_ADDRESS> <path1>")
    sys.exit(1)

theServerAddress = sys.argv[1]
thePath = sys.argv[2]  # Get up to 5 paths from command line arguments
httpPort = 80
maxRequests = 11 # 10 + 1

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((theServerAddress, httpPort))

    for i in range(maxRequests):
        print(f"Request {i + 1} of {maxRequests}")
        request = (
            f"GET {thePath} HTTP/1.1\r\n"
            f"Host: {theServerAddress}\r\n"
            "Connection: keep-alive\r\n"
            "\r\n"
        )

        print(">|")
        print(request, end="")
        print("|<")

        s.sendall(request.encode("utf-8"))

        data = s.recv(4096)
        print("recv()")

        response_text = data.decode(errors="ignore")
        headers_end = response_text.find("\r\n\r\n")

        headers = response_text[:headers_end]

        content_length = 0

        for line in headers.split("\r\n"):
            if "Content-Length:" in line:
                content_length = int(line.split(":")[1].strip())
                break

        print(f"Total Bytes expected from the Server: {content_length}")

        body_already_received = data[headers_end + 4 :]
        total_received_bytes = len(body_already_received)

        while total_received_bytes < content_length:
            chunk = s.recv(4096)
            print("recv()")
            total_received_bytes += len(chunk)

        print(f"Total Bytes Read: {total_received_bytes}")

        if i < maxRequests - 1:
            time.sleep(1)