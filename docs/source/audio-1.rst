Audio 1
=======

In this lesson you will be introduced to using Audio in Python. We will
concentrate on two well-established libraries:
*pydub* in the AUDIO 1  and *pyaudio* in Audio 2

*pydub*
-------
*pydub* allows you to manipulate audio with a simple and easy high level interface. It requires the installation of
dependencies in your system (not your python environment).

    | Follow installation instructions here https://github.com/jiaaro/pydub#installation


Get Pydub
^^^^^^^^^
Import *pydub* into your IDE using the following command::

    pip install pydub

-
    | Full docs for *pydub* can be found here: https://pydub.com/

1. *Hello pydub*
^^^^^^^^^^^^^^^^^^^^^^^
    | Open a new python file in your IDE (or open audio-pydub-1.py).

Import pydub::

    from pydub import AudioSegment
    from pydub.playback import play

Create an pydub audio segment object and fill it with your audio file::

    song = AudioSegment.from_file("giant_steps_35554253331221.wav")  # replace insert_filename_here with your audio file

Play the song::

    play(song)

2. Pydub Creative example
^^^^^^^^^^^^^^^^^^^^^^^^^
In this exercise we will take an audio file and manipulate it using
tape-style manipulations (speed, slice, backwards etc)

    | Open a new python file in your IDE (or open audio-pydub-2.py).

# Import Python modules
from random import randrange

# Import pydub
from pydub import AudioSegment
from pydub.playback import play

# Create an pydub audio segment object and fill it with your audio file
song = AudioSegment.from_file("insert_filename_here.wav")  # replace insert_filename_here with your audio file

# Find the duration
duration_in_milliseconds = len(song)

# Randomly slice the song (needs to be an integer)
start_point = randrange(int(duration_in_milliseconds / 2))
endpoint = randrange(int(start_point + (duration_in_milliseconds / 2)))

# Remove parts of song outside slice
sliced_song = song[start_point:endpoint]

# 2 sec fade in, 3 sec fade out (notice we make a unique version for each mod)
fade_sliced_song = sliced_song.fade_in(2000).fade_out(3000)

# Reverse the song as a new file
backwards_fade_sliced_song = fade_sliced_song.reverse()

# Speed up 2x as a new file
fast_backwards_fade_sliced_song = backwards_fade_sliced_song.speedup(2)

# Play the song
play(fast_backwards_fade_sliced_song)
