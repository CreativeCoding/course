"""
Example taken from https://github.com/CristiFati/pyaudio/blob/master/examples/record.py
"""

# import python modules
import wave

# import pyaudio modules
import pyaudio

# declare constants
CHUNK = 1024  # size of audio chunk per sample
FORMAT = pyaudio.paInt16  # 16 Bit integer = CD quality
CHANNELS = 1  # mono
RATE = 44100  # 44.1kHz = CD quality
RECORD_SECONDS = 5  # duration

#  open a blank file and get ready to fill it
with wave.open('output.wav', 'wb') as wf:
    # start a pyaudio object and set params
    p = pyaudio.PyAudio()
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)

    # open a stream and start filling the pyaudio object
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)

    # write the chunks every cycle to the blank wave file
    print('Recording...')
    for _ in range(0, RATE // CHUNK * RECORD_SECONDS):
        # writeframes!!
        wf.writeframes(stream.read(CHUNK))
    print('Done')

    # close the stream
    stream.close()
    # and terminate the audio object like a grown up
    p.terminate()
