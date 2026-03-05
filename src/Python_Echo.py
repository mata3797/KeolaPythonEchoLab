import sys
import socket

iPort = 36001
sHost = ''

# check that sys.argv contains 3 arguments
# print a usage message and terminate if not
if len(sys.argv) != 3:
    print("Usage: python3 src/Python_Echo.py <IP_ADDRESS> <PORT>")
    sys.exit(1)

# get the sAddr and iPort from the sys.argv
sHost = sys.argv[1]
iPort = int(sys.argv[2])

# use with to open a socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # bind
    s.bind((sHost, iPort))

    # listen
    s.listen()
    print(f"Server is listening on {sHost}:{iPort}...")

    # accept
    conn, addr = s.accept()

    # once a connection is found
    # loop to receive data, print data to the screen,
    # and echo data back to sender
    # terminate the loop once receive returns no data.
    with conn:
        print(f"Connected by {addr}")
        while True:
            # read data from the connection
            data = conn.recv(1024)

            # if no data is received, break the loop
            if not data:
                break

            # convert the bytearray to a str
            message = data.decode()

            # get the prepared message
            echo_message = "BACK:" + message

            # print the messages
            print(f"Received from {addr}: {message}")
            print(f"Echoing: {echo_message}")

            # convert to bytearray and send back to the sender
            conn.sendall(echo_message.encode())