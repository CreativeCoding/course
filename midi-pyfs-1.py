# Import python modules
import fluidsynth
from time import sleep

# activate (instantiate) the fluidsynth object in python
fs = fluidsynth.Synth()
fs.start()  # you may need to use 'start(driver=dsound)' driver in Windows or 'start(driver=alsa)' in linux

# locate the sf2 file and load into the fluidsynth object
sfid = fs.sfload(r'GeneralUser GS v1.471.sf2')  # replace path as needed

# select a sound to play
fs.program_select(0, sfid, 0, 0)

# make some notes
fs.noteon(0, 50, 30)
fs.noteon(0, 57, 30)
fs.noteon(0, 66, 30)

# hold for 2 seconds
sleep(2.0)

# stop the notes
fs.noteoff(0, 50)
fs.noteoff(0, 57)
fs.noteoff(0, 66)

# wait for a bit
sleep(1)

# it is good practice to collapse the object once you have completed the whole task.
# In this case it was a small task.
fs.delete()
