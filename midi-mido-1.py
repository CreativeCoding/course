# Import python modules
from mido.messages import Message
import fluidsynth
from time import sleep

# activate (instantiate) the fluidsynth object in python
fs = fluidsynth.Synth()
fs.start()  # you may need to use 'start(driver=dsound)' driver in Windows or 'start(driver=alsa)' in linux

# locate the sf2 file and load into the fluidsynth object
sfid = fs.sfload(r'GeneralUser GS v1.471.sf2')  # replace path as needed

# select a sound to play
fs.program_select(0, sfid, 0, 0)

# Make a midi Message object and call it msg
# This message will be a 'not on' type, with note number 60
msg = Message('note_on', note=60)

# Amend other Message Object parameters
msg.velocity = 90

# Print out the contents of the message object msg
print(msg)

# Parse the Message and play on fluidsynth
if msg.type == "note_on":
    fs.noteon(msg.channel, msg.note, msg.velocity)
    sleep(2)
    fs.noteoff(msg.channel, msg.note)

# Collapse the fs object
fs.delete()

"""
ALTERNATIVE TO FLUIDSYNTH

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
"""