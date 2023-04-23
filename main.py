import socket

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to a remote host
client_socket.connect(('www.google.com', 80))

# check if the socket is closed

status = client_socket.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)

print(f"The status of the socket is {status}")

# close the socket
client_socket.close()
