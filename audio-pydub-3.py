# Import Python Modules
from random import shuffle

# Import Pydub modules
from pydub import AudioSegment
from pydub.utils import make_chunks
from pydub.playback import play

# Import source audio as an Audio Segment in an object
source_audio = AudioSegment.from_file("drum2.aif")

# Declare how many milliseconds you want to slice your source audio into (pydub calculates in millisecs)
chunk_length_ms = 100

# Make a list called chunks of sliced audio
chunks = make_chunks(source_audio, chunk_length_ms)

# Shuffle the chunk list for fun
shuffle(chunks)

# Make a new empty Audio segment object (to fill with the randomised chunks)
new_audio_file = AudioSegment.empty()

# Iterate through the list of chunks and add to empty audio segment object
for i, chunk in enumerate(chunks):
   new_audio_file += chunk

# Playback your new audio
play(new_audio_file)

# Save new file as a wav::
new_audio_file.export("test", format="wav")
