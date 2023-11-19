MIDI 1
======

In this lesson you will be introduced to using Midi in Python. We will concentrate on two well-established libraries:
*Mingus* and *Music21*

We will be using an internal synthesiser too, so we need to install *fluidsynth*.

Follow the instructions here https://github.com/FluidSynth/fluidsynth

*FluidSynth* is a MIDI synthesizer which uses SoundFont (.SF2) files to generate audio.
To get it to make a sound you will need one of these files (look here: http://www.hammersound.net,
go to Sounds -> Soundfont Library -> Collections)

Once you have *fluidsynth* and have tested it works, you can move forward with the lesson.

Mingus
------
Get *mingus*
^^^^^^^^^^^^

Import mingus into your IDE using the following command::

    pip install mingus
Full docs for *mingus* can be found here https://bspaans.github.io/python-mingus/index.html

*Hello Mingus*
^^^^^^^^^^^^^^
This first lesson will concentrate getting mingus to play a single note.

First import mingus into a new python script in your IDE::
    from mingus.midi import fluidsynth

Then initialise


    fluidsynth.init("soundfont.SF2")

