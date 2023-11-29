I/O Comms 2
===========

In this lesson we will explore using python for internet comms and streaming. The main low-level
library that we will be using is *socket*.

*socket*
--------
A socket is an interface (gate) for communication between different processes located on the same or different machines.
Python sockets are used for applications that need to communicate over a network: such as web servers, chat applications,
or email clients. The server program listens and handles incoming connections, whilst the client connects to the server
to send and receive data.
Python sockets support both TCP—a reliable protocol that ensures in-order packet delivery, and UDP—a connectionless and
lightweight protocol for applications where packet loss is acceptable.


Get *socket*
^^^^^^^^^^^^
*socket* is already included in python, so no need to install it.

    | Full docs for *socket* can be found here: https://docs.python.org/3/library/socket.html?highlight=socket#module-socket


1. Hello *socket*
------------------
In this example we will use *socket* to reach out (like a ping) and test if a website is up and running.

Import libraries::

    import socket
    import time

Setup all working variables::

    port = 443
    retry = 5
    delay = 1
    timeout = 3

List websites to test::

    ip = ["facebook.com",
          "google.com",
          "fbi.gov",
          "nottingham.ac.uk",
          "digiscore.github.io",
          "garbage.gigo"
          ]

Function that opens an ip Socket::

    def isOpen(ip, port):
        # Instantiate a socket object for a given ip address
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)

        # Try to connect and if successful return a True bool
        try:
            s.connect((ip, int(port)))
            s.shutdown(socket.SHUT_RDWR)
            return True
        except:
            return False
        # Important to close it
        finally:
            s.close()

Function that dispatches socket info to isOpen func and returns results::

    def checkHost(ip, port):
        # Sets condition to False
        is_up = False

        # For a number of trys
        for t in range(retry):
            print(f"Checking {ip}")
            if isOpen(ip, port):
                is_up = True
                break
            else:
                time.sleep(delay)
        return is_up

Function controlling the main loop::

    def main():
        # For each web address in ip list check if it is up and running
        for i in ip:
            if checkHost(i, port):
                print(f"\t\t{i} is UP and running")
                time.sleep(1)

Code starts here::

    if __name__ == "__main__":
        main()

2. Simple client-server
^^^^^^^^^^^^^^^^
In this example



    | Original code taken from https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client


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

3. Streaming audio over IP
^^^^^^^^^^^^^^^^^^^^^^^^^^

"""https://pyshine.com//How-to-send-audio-from-PyAudio-over-socket/"""

######################
# RUN THIS IN TERMINAL
######################

# Import libraries
import socket
import os
import threading
import pyaudio
import pickle
import struct

# Declare all variables and constants
host_name = socket.gethostname()
host_ip = '192.168.1.102'  # socket.gethostbyname(host_name)
print(host_ip)
port = 9611  # socket server port number MUST BE SAME AS SERVER

# Function that connects to the server and stream audio
def audio_stream():
    # Stuff from pyaudio: set chunk size and open a stream
    p = pyaudio.PyAudio()
    CHUNK = 1024
    stream = p.open(format=p.get_format_from_width(2),
                    channels=2,
                    rate=44100,
                    output=True,
                    frames_per_buffer=CHUNK)

    # Instantiate a Socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_address = (host_ip, port - 1)
    print('server listening at', socket_address)

    # Connect to the server
    client_socket.connect(socket_address)
    print("CLIENT CONNECTED TO", socket_address)

    # State operational vars and consts
    data = b""
    payload_size = struct.calcsize("Q")

    # Endless loop for streaming
    while True:
        try:
            # Receive a data package from the server
            while len(data) < payload_size:
                packet = client_socket.recv(4 * 1024)  # 4K
                if not packet:
                    break
                data += packet

            # Calc the size of the package
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("Q", packed_msg_size)[0]
            while len(data) < msg_size:
                data += client_socket.recv(4 * 1024)
            # Strip off the audio chunk
            frame_data = data[:msg_size]
            data = data[msg_size:]
            frame = pickle.loads(frame_data)
            # Write to the pyaudio stream
            stream.write(frame)
        except:
            break

    # Close the socket once completed
    client_socket.close()
    print('Audio closed')
    os._exit(1)

# Make a thread.
t1 = threading.Thread(target=audio_stream, args=())
t1.start()


"""
Original Code from https://pyshine.com//How-to-send-audio-from-PyAudio-over-socket/
"""

######################
# RUN THIS IN YOUR IDE
######################

# Import libraries
import socket
import threading
import wave
import pyaudio
import pickle
import struct

# Declare all variables and constants
host_name = socket.gethostname()
host_ip = '192.168.1.102'  # socket.gethostbyname(host_name)
print(host_ip)
port = 9611   # socket server port number MUST BE SAME AS SERVER

# Function that listens out for client and accepts audio stream
def audio_stream():
    # Instantiate a Socket object
    server_socket = socket.socket()

    # Bind the host address and port together
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host_ip, (port - 1)))

    # configure how many client the server can listen simultaneously
    server_socket.listen(5)

    # Stuff from pyaudio: set chunk size and open the file to stream
    CHUNK = 1024
    wf = wave.open("temp.wav", 'rb')  # Change file path to access YOUR audio file. rb = read

    # Instantiate a pyaudio object
    p = pyaudio.PyAudio()
    print('server listening at', (host_ip, (port - 1)))

    # create a pyaudio stream (do this stuff first so not to break the connection)
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    input=True,
                    frames_per_buffer=CHUNK)

    # Accept the connection (handshake)
    client_socket, addr = server_socket.accept()

    data = None

    # Endless loop
    while True:
        if client_socket:

            # Stream the audio file a chunk at a time
            while True:
                data = wf.readframes(CHUNK)

                # Pack into a pickle file
                a = pickle.dumps(data)

                # send chunk (as pickle) with length
                message = struct.pack("Q", len(a)) + a

                # Send it off
                client_socket.sendall(message)

# Make a thread.
t1 = threading.Thread(target=audio_stream, args=())
t1.start()

