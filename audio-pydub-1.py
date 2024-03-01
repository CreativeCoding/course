# Import pydub
from pydub import AudioSegment
from pydub.playback import play, _play_with_simpleaudio

# Create an pydub audio segment object and fill it with your audio file
song = AudioSegment.from_wav("giant_steps_35554253331221.wav")  # replace insert_filename_here with your audio file

# Play the song
play(song)
_play_with_simpleaudio(song)