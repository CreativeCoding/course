# Import python modules
from mingus.midi import fluidsynth
from mingus.containers import Note
from time import sleep

# initiate Fluidsynth
fluidsynth.init("GeneralUser GS v1.471.sf2")

# Create a note object and give it pitch C in octave 5
mynote = Note("C-5")

# change some other parameters of the mynote object
mynote.velocity = 50
mynote.channel = 5
mynote.note = "D-5"

# get Fluidsynth to play mynote for 1 second
fluidsynth.play_Note(mynote)
sleep(1)    # pause for 1 second
fluidsynth.stop_Note(mynote)
