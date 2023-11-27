"""
Example taken from:
https://deepgram.com/learn/best-python-audio-manipulation-tools
"""
# Import libraries
import pyaudio
import wave

# Declare consts
filename = 'CHANGE_FILENAME.wav'
chunk = 1024

# Open the file
wf = wave.open(filename, 'rb')

# Instantiate a pyaudio object
pa = pyaudio.PyAudio()

# create stream using info from the file
stream = pa.open(format=pa.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True
                 )

# Read starting frame of data (NB Readframes!!)
data = wf.readframes(chunk)

# while the data isn't empty
while data != b'':
    # Send each chunk from the wav file to the pyaudio output stream
    stream.write(data)
    # Read next frames as the loop
    data = wf.readframes(chunk)

# cleanup
stream.close()
pa.terminate()
