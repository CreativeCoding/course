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
