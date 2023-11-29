Audio 2
=======

In this lesson you will be introduced to using Audio streams in Python. In this session we will
concentrate on *pyaudio*

*pyaudio*
-------
PyAudio provides Python bindings for PortAudio v19, the cross-platform audio I/O library.
With *pyaudio*, you can easily use Python to play and record audio on a variety of platforms,
such as GNU/Linux, Microsoft Windows, and Apple macOS. It allows for complicated and 'under the hood'
tinkering and manipulation of audio that *pydub*. Plus it will allow you to stream input audio.

    | Follow installation instructions here https://people.csail.mit.edu/hubert/pyaudio/


Get *pyaudio*
^^^^^^^^^^^^^
To import *pyaudio* into your IDE you first need to install *portaudio* into your system.

This differs on OS, so follow the guidance here::

    https://people.csail.mit.edu/hubert/pyaudio/

-
    | Full docs for *pyaudio* can be found here: https://people.csail.mit.edu/hubert/pyaudio/docs/

1. *Hello pyaudio*
^^^^^^^^^^^^^^^^^^^

    | reference: audio-pyaudio-1.py

Now that you have installed *pyaudio* we can run a simple
PyAudio example that plays a wav file. Notice that it now works in chunks
or samples, and is a closer process to how digital audio is stored.


    | Example taken from: https://deepgram.com/learn/best-python-audio-manipulation-tools

Import libraries::

    import pyaudio
    import wave

Declare consts::

    filename = 'CHANGE_FILENAME.wav'
    chunk = 1024

Open the file::

    wf = wave.open(filename, 'rb')

Instantiate a pyaudio object::

    pa = pyaudio.PyAudio()

Create stream using info from the file::

    stream = pa.open(format=pa.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True
                     )

Read starting frame of data::

    data = wf.readframes(chunk)

While the data isn't empty::

    while data != b'':
        # Send each chunk from the wav file to the pyaudio output stream
        stream.write(data)
        # Read next frames as the loop (NB readframes!!)
        data = wf.readframes(chunk)

Cleanup::

    stream.close()
    pa.terminate()


2. Creative Example
^^^^^^^^^^^^^^^^^^^
In this example we will record the input from the laptop microphone as
a series of samples, and then write these to a file on disk.

    | reference: audio-pyaudio-2.py


Example taken from https://github.com/CristiFati/pyaudio/blob/master/examples/record.py


Import python modules::

    import wave

Import pyaudio modules::

    import pyaudio

Declare constants::

    CHUNK = 1024  # size of audio chunk per sample
    FORMAT = pyaudio.paInt16  # 16 Bit integer = CD quality
    CHANNELS = 1  # mono
    RATE = 44100  # 44.1kHz = CD quality
    RECORD_SECONDS = 5  # duration

Open a blank file and get ready to fill it::

    with wave.open('output.wav', 'wb') as wf:
        # start a pyaudio object and set params
        p = pyaudio.PyAudio()
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)

Open a stream and start filling the pyaudio object::

    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)

Write the chunks every cycle to the blank wave file::

    print('Recording...')
    for _ in range(0, RATE // CHUNK * RECORD_SECONDS):
        # writeframes!!
        wf.writeframes(stream.read(CHUNK))
    print('Done')

Close the stream::

    stream.close()
    # and terminate the audio object like a grown up
    p.terminate()
3. Advanced creative usage
^^^^^^^^^^^^^^^^^^^^^^^^^^

In this exmaple we will analyis eth incoming microphone signal and calculate
fundamental pitch, midi notes and amplitude.

    | Reference audio-pyaudio-3.py


Import python libraries::

    import numpy as np
    import math
    from threading import Thread
    from time import time

Import Pyaudio library::

    import pyaudio


Build an object to manage all audio analysis::

    class Audio:
        def __init__(self):
            """
            Class object that controls audio listening
            and analysis.
            """
            # set up mic listening func
            self.CHUNK = 2 ** 11
            self.RATE = 44100
            self.p = pyaudio.PyAudio()
            self.stream = self.p.open(format=pyaudio.paInt16,
                                      channels=1,
                                      rate=self.RATE,
                                      input=True,
                                      frames_per_buffer=self.CHUNK)

            # initiate the data dictionary
            self.notes = ['a', 'bf', 'b', 'c', 'df', 'd', 'ef', 'e', 'f', 'gf', 'g', 'af']
            self.audio_dict = {"amplitude": 0,
                               "freq": 0,
                               "midinote": []
                               }

Start a thread to spin the audio analyser::

    def start(self):
        print("mic listener: started!")
        # use threading to spin this plate
        audio_thread = Thread(target=self.audio_analyser)
        audio_thread.start()

Listens to the live microphone input::

    def audio_analyser(self):
        # Get now time and calc end of test time
        length = 5000  # milliseconds
        nowtime = time()
        endtime = nowtime + length

        # For the duration of the test
        while time() <= endtime:
            data = np.frombuffer(self.stream.read(self.CHUNK,
                                                  exception_on_overflow=False),
                                 dtype=np.int16)
            peak = np.average(np.abs(data)) * 2

            # If the sound is loud enough
            if peak > 1000:
                bars = "#" * int(50 * peak / 2 ** 16)

                # Calculates the frequency from the stream
                data = data * np.hanning(len(data))
                fft = abs(np.fft.fft(data).real)
                fft = fft[:int(len(fft) / 2)]
                freq = np.fft.fftfreq(self.CHUNK, 1.0 / self.RATE)
                freq = freq[:int(len(freq) / 2)]
                freqPeak = freq[np.where(fft == np.max(fft))[0][0]] + 1

                # get midinote from freqPeak
                midinote = self.freq_to_note(freqPeak)

                # Shows the peak frequency and the bars for the amplitude
                print(f"peak frequency: {freqPeak} Hz, mididnote {midinote}:\t {bars}")

                self.audio_dict['freq'] = freqPeak
                self.audio_dict['midinote'] = midinote
                self.audio_dict['amplitude'] = peak

Calculate note using Neoscore format::

    def freq_to_note(self, freq: float) -> list:
        """Converts frequency into midi note and octave.
        formula taken from https://en.wikipedia.org/wiki/Piano_key_frequencies

        returns: str neonote (neoscore format e.g. "fs''")
        """

        note_number = 12 * math.log2(freq / 440) + 49
        note_number = round(note_number)
        note_position = (note_number - 1) % len(self.notes)
        neonote = self.notes[note_position]
        octave = (note_number + 8) // len(self.notes)

        # if octave out of range then make it middle C octave
        if 2 <= octave <= 6:

            # add higher octave indicators "'"
            if octave > 4:
                ticks = octave - 4
                for tick in range(ticks):
                    neonote += "'"

            # add lower octave indicators ","
            elif octave < 4:
                if octave == 3:
                    neonote += ","
                elif octave == 2:
                    neonote += ",,"

        return [neonote]

Read the shared dictionary::

    def read(self) -> list:
        """
        returns current dictionary as list, as a single quaver
        """
        audio_list = []
        audio_list.append("midi")  # type
        if self.audio_dict['amplitude'] > 1000:
            audio_list.append(self.audio_dict.get("midinote"))  # pitch
        else:
            audio_list.append([])  # rest
        audio_list.append(0.5)  # duration
        return audio_list

Terminate all streams like a grown up::

    def terminate(self):
        """
        safely terminates all streams
        """
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

Start the script here::

    if __name__ == "__main__":
        # Start audio listener object
        mic = Audio()
        mic.start()

        # Terminate streams like a grown up
        mic.terminate()
