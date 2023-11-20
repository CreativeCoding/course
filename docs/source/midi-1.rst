MIDI 1
======

In this lesson you will be introduced to using Midi in Python. We will concentrate on three well-established libraries:
*pyfluidsynth*, *mido* and *music21*

pyfluidsynth
-------------
Get Fluidsynth
^^^^^^^^^^^^^^

*pyfluidsynth* is a python binding to the more universal *fluidsynth* library. Fluidsynth
is an internal synthesiser, so we need to install *fluidsynth* into the computer not the python environment.

Follow the instructions here https://github.com/FluidSynth/fluidsynth/wiki/Download

*FluidSynth* is a MIDI synthesizer which uses SoundFont (.SF2) files to generate audio.
To get it to make a sound you will need one of these files (look here: https://github.com/FluidSynth/fluidsynth/wiki/SoundFont
for simplicity we are using *GeneralUser GS v1.471.sf2* ).
Put this sf2 file into your 'project' folder.

testing fluidsynth
^^^^^^^^^^^^^^^^^^
Once you have installed *fluidsynth* you now need to test it works.

    1. download this midi file into the same 'project' folder as the sf2 file https://www.mfiles.co.uk/downloads/book1-prelude01.mid
    2. open a terminal/ command prompt and go to the 'project' folder
    3. run this Bash command::

    fluidsynth GeneralUser GS v1.471.sf2 book1-prelude01.mid

This will play the Bach midi file in *fluidsynth* using the sf2 file as the general midi sound source.

Get pyfluidsynth
^^^^^^^^^^^^^^^^
Once you have installed *fluidsynth* and have tested it works, you can move forward with the lesson. But,
first we need to import the python binding library for fluidsynth::

    pip install pyfluidsynth

1. *Hello pyfluidsynth*
^^^^^^^^^^^^^^^^^^^^^^^
Open a new python file in your IDE (or open midi-pyfs-1.py).

Import python modules::

    import fluidsynth
    from time import sleep

Activate (instantiate) the fluidsynth object in python::

    fs = fluidsynth.Synth()
    fs.start()  # you may need to use 'start(driver=dsound)' driver in Windows or 'start(driver=alsa)' in linux

Locate the sf2 file and load into the fluidsynth object::

    sfid = fs.sfload(r'GeneralUser GS v1.471.sf2')  # replace path as needed

Select a sound to play::

    fs.program_select(0, sfid, 0, 0)

Make some notes::

    fs.noteon(0, 50, 30)
    fs.noteon(0, 57, 30)
    fs.noteon(0, 66, 30)

Hold for 2 seconds::

    sleep(2.0)

Stop the notes::

    fs.noteoff(0, 50)
    fs.noteoff(0, 57)
    fs.noteoff(0, 66)

Wait for a bit::

    sleep(1)

It is good practice to collapse the object once you have completed the whole task.
In this case it was a small task::

    fs.delete()



Mido
------
Get *mido*
^^^^^^^^^^^^

Import mingus into your IDE using the following command::

    pip install mido

Full docs for *mingus* can be found here https://mido.readthedocs.io/en/stable/

1. *Hello Mido*
^^^^^^^^^^^^^^^^^
midi-mido-1.py

This first lesson will concentrate getting mido to play a single note.

First import some mingus methods and sleep into a new python script in your IDE::

    from mingus.midi import fluidsynth
    from mingus.containers import Note
    from time import sleep

Then initialise the synth::

    fluidsynth.init("soundfont.SF2")

Now build a note object::

    mynote = Note("C-5")

This will instantiate a Note object (called *mynote*) and assign it the pitch C in 5th octave.
We can modify *mynote* with other Note class parameters such as midi channel, velocity, and change the pitch::

    mynote.velocity = 50
    mynote.channel = 5
    mynote.note = "D-5"

Next we can play *mynote* on Fluidsynth, but will need to stop with a stop command::

    fluidsynth.play_Note(mynote)
    sleep(1) # pause for 1 second
    fluidsynth.stop_Note(mynote)

When you run this code you should hear a piano note sound for 1 second.

2. Mingus Creative example
^^^^^^^^^^^^^^^^^^^^^^^^^^
Linked to midi-mingus-2.py


