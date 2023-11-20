# Import python modules
import random
import time
import mido
from mido.messages import Message
import fluidsynth

# activate (instantiate) the fluidsynth object in python
fs = fluidsynth.Synth()
fs.start()  # you may need to use 'start(driver=dsound)' driver in Windows or 'start(driver=alsa)' in linux

# locate the sf2 file and load into the fluidsynth object
sfid = fs.sfload(r'GeneralUser GS v1.471.sf2')  # replace path as needed

# select a sound to play
fs.program_select(0, sfid, 0, 0)

# Declare operational params
# A pentatonic scale
notes = [60, 62, 64, 67, 69, 72]
durations = [1, 0.5, 0.6, 0.3]

# Create a function that plays the midi not to fluidsynth
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

# While on an infinite loop
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
