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

Import Python modules::

    from random import randrange

Import pydub::

    from pydub import AudioSegment
    from pydub.playback import play

Create an pydub audio segment object and fill it with your audio file::

    song = AudioSegment.from_file("insert_filename_here.wav")  # replace insert_filename_here with your audio file

Find the duration::

    duration_in_milliseconds = len(song)

Randomly slice the song (needs to be an integer)::

    start_point = randrange(int(duration_in_milliseconds / 2))
    endpoint = randrange(int(start_point + (duration_in_milliseconds / 2)))

Remove parts of song outside slice::

    sliced_song = song[start_point:endpoint]

Add 2 sec fade in, 3 sec fade out (notice we make a unique version for each mod)::

    fade_sliced_song = sliced_song.fade_in(2000).fade_out(3000)

Reverse the song as a new file::

    backwards_fade_sliced_song = fade_sliced_song.reverse()

Speed up 2x as a new file::

    fast_backwards_fade_sliced_song = backwards_fade_sliced_song.speedup(2)

Play the song::

    play(fast_backwards_fade_sliced_song)

3. Pydub API
^^^^^^^^^^^
The API and comprehensive docs offer many examples of *pydub*'s usability and OOP construction.

Here we are going to explore some of its API functions and create an audio splicer.

Import Python Modules::

    from random import shuffle

Import Pydub modules::

    from pydub import AudioSegment
    from pydub.utils import make_chunks
    from pydub.playback import play

Import source audio as an Audio Segment in an object::

    source_audio = AudioSegment.from_file("drum2.aif")

Declare how many milliseconds you want to slice your source audio into (pydub calculates in millisecs)::

    chunk_length_ms = 100

Make a list called chunks of sliced audio::

    chunks = make_chunks(source_audio, chunk_length_ms)

Shuffle the chunk list for fun::

    shuffle(chunks)

Make a new empty Audio segment object (to fill with the randomised chunks)::

    new_audio_file = AudioSegment.empty()

Iterate through the list of chunks and add to empty audio segment object::

    for i, chunk in enumerate(chunks):
       new_audio_file += chunk

Playback your new audio::

    play(new_audio_file)

Save new file as a wav::

    new_audio_file.export("test", format="wav")

