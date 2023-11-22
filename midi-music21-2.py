from music21 import converter
from random import shuffle
import fluidsynth
from time import sleep


# activate (instantiate) the fluidsynth object in python
fs = fluidsynth.Synth()
fs.start()  # you may need to use 'start(driver=dsound)' driver in Windows or 'start(driver=alsa)' in linux

# locate the sf2 file and load into the fluidsynth object
sfid = fs.sfload(r'GeneralUser GS v1.471.sf2')  # replace path as needed

# select a church organ to make the sound
fs.program_select(0, sfid, 0, 19)


# This defines the function
def get_midi_bits(mf: str) -> list:
    """Takes a path to a midifile, converts to Music21 stream
    then parses the metadata for each note, rest and chord into
    neoscore-ready format:
    [[pitch list: neoscore notes], duration as quarter note]

    returns: list"""

    # convert it to music21 format
    score_in = converter.parseFile(mf)

    # make a blank list
    bits = []

    # parse through the midi file and extract only notes, rests, chords
    for msg in score_in.recurse().notesAndRests:

        # if note length is not 0 then convert to neoscore
        if msg.duration.quarterLength != 0:

            try:
                p = msg.name
                o = msg.octave
                d = msg.quarterLength
                bits.append([f"{p}_{o}", d])
                print(p, d)

            except:
                print(f"Error caused by {msg}")

    # print(bits)
    return bits

def play_midi_bits(bits: list):
    for n in bits:
        print(n)
        pitch = n[0]
        duration = n[1]

        # midi note cal
        midi_note = calc_midi_note(pitch)
        fs.noteon(0, midi_note, 70)
        sleep(duration/2)
        fs.noteoff(0, midi_note)

def calc_midi_note(midstr: str):
    """
    https://stackoverflow.com/questions/13926280/musical-note-string-c-4-f-3-etc-to-midi-note-value-in-python
    """
    Notes = [["C"], ["C#", "D-"], ["D"], ["D#", "E-"], ["E"], ["F"], ["F#", "G-"], ["G"], ["G#", "A-"], ["A"],
             ["A#", "B-"], ["B"]]
    answer = 0
    i = 0
    # Note
    letter = midstr.split('_')[0].upper()
    for note in Notes:
        for form in note:
            if letter.upper() == form:
                answer = i
                break
        i += 1
    # Octave
    answer += (int(midstr[-1])) * 12
    return answer

#  Code starts here
if __name__ == "__main__":
    # Send a Midifile path to
    midi_bits = get_midi_bits("book1-prelude01.mid")
    shuffle(midi_bits)
    play_midi_bits(midi_bits)
