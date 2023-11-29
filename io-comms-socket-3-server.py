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
