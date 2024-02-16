MIDI 1
======

In this lesson you will be introduced to using Midi in Python. We will concentrate on three well-established libraries:
*pyfluidsynth* and *mido* in the MIDI 1 session and *music21* in MIDI 2

*pyfluidsynth*
-------------
Get Fluidsynth
^^^^^^^^^^^^^^

*pyfluidsynth* is a python binding to the more universal *fluidsynth* library. Fluidsynth
is an internal synthesiser, so we need to install *fluidsynth* into the computer not the python environment.

The easiet way to manage these computer packages is to install a package manager such as:

    - HomeBrew (MacOS) https://brew.sh/
    - Chocolatey (Windows) https://chocolatey.org/   (help video here https://www.youtube.com/watch?v=hfgZYpo5moA)


Follow the instructions here:

    - Raw import https://github.com/FluidSynth/fluidsynth/wiki/Download
    - Homebrew https://formulae.brew.sh/formula/fluid-synth
    - Chocolatey https://community.chocolatey.org/packages/fluidsynth

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
    | Open a new python file in your IDE (or open midi-pyfs-1.py).

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



*Mido*
------
*Fluidsynth* is very good at playing assigned notes on a software synth. But if you want more control over your MIDI signals,
manage live MIDI signals to and from external devices, manipulate command control parameters, perhaps create files in MIDI,
then *mido* would be a better library.

Get *mido*
^^^^^^^^^^^^

Import *mido* into your IDE using the following command::

    pip install mido

    | Full docs for *mido* can be found here https://mido.readthedocs.io/en/stable/

1. *Hello Mido*
^^^^^^^^^^^^^^^^^
midi-mido-1.py

This first lesson will concentrate getting mido to play a single note.

First import python modules::

    from mido.messages import Message
    import fluidsynth
    from time import sleep

Activate (instantiate) the fluidsynth object in python::

    fs = fluidsynth.Synth()
    fs.start()  # you may need to use 'start(driver=dsound)' driver in Windows or 'start(driver=alsa)' in linux

Locate the sf2 file and load into the fluidsynth object::

    sfid = fs.sfload(r'GeneralUser GS v1.471.sf2')  # replace path as needed

Select a sound to play::

    fs.program_select(0, sfid, 0, 0)

Make a midi Message object and call it msg.
This message will be a 'note on' type, with note number 60::

    msg = Message('note_on', note=60)

Amend other Message Object parameters, in this case velocity::

    msg.velocity = 90

Print out the contents of the message object msg::

    print(msg)

Parse the Message and play on fluidsynth::

    if msg.type == "note_on":
        fs.noteon(msg.channel, msg.note, msg.velocity)
        sleep(2)
        fs.noteoff(msg.channel, msg.note)

ALTERNATIVE TO FLUIDSYNTH
^^^^^^^^^^^^^^^^^^^^^^^^^
With the above exmaple, it is not achieveing much more than can be achieved with
*pyfluidsynth*. To understand why *mido* is so useful, we need to plug in a midi port device (
e.g. virtual instrument in Garageband, or an external synth) and use the following code::

    portname = "INSERT PORT NAME HERE"
    with mido.open_output(portname, autoreset=True) as port:
        print(f'Using {port}')

        on = Message('note_on', note=note)
        print(f'Sending {on}')
        port.send(on)
        time.sleep(0.05)

        off = Message('note_off', note=note)
        print(f'Sending {off}')
        port.send(off)
        time.sleep(0.1)


    2. Mido Creative example
    ^^^^^^^^^^^^^^^^^^^^^^^^^^
    | Linked to midi-mido-2.py

This example will loop through a random note sequence.

Import python modules::

    import random
    import time
    import mido
    from mido.messages import Message
    import fluidsynth

Activate (instantiate) the fluidsynth object in python::

    fs = fluidsynth.Synth()
    fs.start()  # you may need to use 'start(driver=dsound)' driver in Windows or 'start(driver=alsa)' in linux

Locate the sf2 file and load into the fluidsynth object::

    sfid = fs.sfload(r'GeneralUser GS v1.471.sf2')  # replace path as needed

Select a sound to play::

    fs.program_select(0, sfid, 0, 0)

Declare operational params
A pentatonic scale and triplets::

    notes = [60, 62, 64, 67, 69, 72]
    durations = [1, 0.5, 0.6, 0.3]

Create a function that plays the midi not to fluidsynth::

    def fs_player(ftype, fnote, fvelocity=0):
        # if the incoming type is a note
        if ftype == "note_on":
            fs.noteon(chan=0,
                      key=fnote,
                      vel=fvelocity
                      )
        # if the incoming type is not off
        elif ftype == "note_off":
            fs.noteoff(chan=0,
                       key=fnote
                       )
        # else there is an error
        else:
            print("Error")

While on an infinite loop::

    while True:
        # make some random choices about note, duration and velocity
        note = random.choice(notes)
        duration = random.choice(durations)
        velocity = random.randrange(30, 100)

        # create an on Message object
        on = Message('note_on',
                     note=note,
                     velocity=velocity
                     )
        # send to the fs_player function to sound
        print(f'Sending {on}')
        fs_player(ftype="note_on",
                  fnote=note,
                  fvelocity=velocity)
        # sleep for the rhythm duration
        time.sleep(duration)

        # turn the note off
        off = Message('note_off',
                      note=note
                      )
        print(f'Sending {off}')
        fs_player("note_off",
                  fnote=note)

3. Mido API
^^^^^^^^^^^
The API and comprehensive docs offer many examples of *mido*'s usability and OOP construction.

Here is one example of how to build and save a midifile (taken verbatim from https://mido.readthedocs.io/en/stable/files/midi.html#creating-a-new-file):

1. import the methods from mido::

    from mido import Message, MidiFile, MidiTrack

2. create 2 types of objects: a midifile, and a midi track which we will fill with Message objects::

    mid = MidiFile()
    track = MidiTrack()
3. add (append) the track object into the midifil object::

    mid.tracks.append(track)
4. add (append) midi messages to the track object::

    track.append(Message('program_change', program=12, time=0))
    track.append(Message('note_on', note=64, velocity=64, time=32))
    track.append(Message('note_off', note=64, velocity=127, time=32))
5. finally save the midifile object, which now contains 1 track with 3 messages::

    mid.save('new_song.mid')

