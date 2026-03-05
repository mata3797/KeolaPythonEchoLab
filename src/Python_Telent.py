import socket
import sys

def start_tcp_client(sAddr, iPort):

    # Create a TCP/IP socket
    # define AF_INET:
    # define SOCK_STREAM:

    
    # Create tuple of the address and port
    
    # connect to create the socket
    
    # look out for exceptions
    try:
        # get str from the keyboard, convert to byte array
        sMessage = input('Enter messgage: ')
        
        while ('QUIT' != sMessage):
            # convert str to bytearray
            
            # send message to the socket
            
            # receive data (look for 1024 bytes)
            
            # get str from the keyboard, convert to byte array

            pass
            

    finally:
        # use a finally clause to close socket 
        # runs even if an exception occurs
        pass


#########################################################

sAddr = ''
iPort = 36001


# check that sys.argv contains 3 arguments
# print a usage message and terminate if not
if len(sys.argv) != 3:
    print("Usage: python3 src/Python_Telnet.py <IP_ADDRESS> <PORT>")
    sys.exit(1)

# get the sAddr and iPort from the sys.argv
sAddr = sys.argv[1]
iPort = int(sys.argv[2]) # Convert port string to integer

# Start the TCP client
start_tcp_client(sAddr, iPort)