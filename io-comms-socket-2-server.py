"""
Original code taken from https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client
"""

######################
# RUN THIS IN YOUR IDE
######################


# Import libraries
import socket

# Function that operates as a server - can take up to 3 clients at a time
def server_program():
    # get the hostname (your computer for this test)
    host = socket.gethostname()
    print(f'Hostname = {host}')
    port = 5000  # initiate port no above 1024

    # Instantiate a Socket object
    server_socket = socket.socket()

    # Bind the host address and port together
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))

    # configure how many client the server can listen simultaneously
    server_socket.listen(3)

    # Accept the connection (handshake)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))

    # Endless loop
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()

        # if data is not received break
        if not data:
            break
        print(f"Received {str(data)} from connected user")

        # Send data back
        data = input(' -> ')
        conn.send(data.encode())  # send data to the client

    # close connection once finished
    conn.close()  # close the connection

# Code starts here if called directly (use IDE)
if __name__ == '__main__':
    server_program()
