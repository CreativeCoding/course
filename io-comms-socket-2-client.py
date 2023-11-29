"""
original code taken from https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client
"""

######################
# RUN THIS IN TERMINAL
######################

# Import libraries
import socket

# Function that manages the client side
def client_program():
    # get the hostname (your computer for this test)
    host = socket.gethostname()  # as both code is running on same pc
    print(f'Hostname = {host}')
    port = 5000  # socket server port number MUST BE SAME AS SERVER

    # Instantiate a Socket object
    client_socket = socket.socket()
    # connect to the server
    client_socket.connect((host, port))

    # Write a message to the server
    message = input(" -> ")

    # If 'bye' then client will close con, otherwise
    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print(f'Received {data} from server')  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection

# Code starts here if called directly (use terminal)
if __name__ == '__main__':
    client_program()
