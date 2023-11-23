# import Python modules
from music21 import converter
from random import shuffle
import fluidsynth
from time import sleep
from threading import Thread


# activate (instantiate) the fluidsynth object in python
fs = fluidsynth.Synth()
fs.start()  # you may need to use 'start(driver=dsound)' driver in Windows or 'start(driver=alsa)' in linux

# locate the sf2 file and load into the fluidsynth object
sfid = fs.sfload(r'GeneralUser GS v1.471.sf2')  # replace path as needed

# select a church organ to make the sound
fs.program_select(0, sfid, 0, 19)

def get_midi_bits(mf) -> list:
    """
    Takes a path to a midifile, converts to Music21 stream
    then parses the metadata for each note, rest and chord into a list.

    :param mf:
    :return: list of individual note data
    """

    # convert it to music21 format
    score_in = converter.parseFile(mf)

    # make a blank list
    bits = []

    # parse through the midi file and extract only notes, rests, chords
    for msg in score_in.recurse().notesAndRests:

        # if note length is not 0 then convert to extract note information
        if msg.duration.quarterLength != 0:
            # Get note name, octave and duration
            try:
                p = msg.name
                o = msg.octave
                d = msg.quarterLength
                bits.append([f"{p}_{o}", d])
                print(p, d)

            except:
                print(f"Error caused by {msg}")

    # Send this list back to where this function was called
    return bits

def calc_midi_note(midstr: str) -> int:
    """
    Calculates the midi number for a given Music21 notes string, format pitch_octave.
    Taken directly from:
    https://stackoverflow.com/questions/13926280/musical-note-string-c-4-f-3-etc-to-midi-note-value-in-python
    """
    # Declare the note list as enharmonic spellings (NB starting at C!!)
    notes = [["C"], ["C#", "D-"], ["D"], ["D#", "E-"], ["E"], ["F"], ["F#", "G-"], ["G"], ["G#", "A-"], ["A"],
             ["A#", "B-"], ["B"]]

    # declare variables
    answer = 0
    i = 0

    # Get the note through bubble search of the notes list until match
    letter = midstr.split('_')[0].upper()
    for note in notes:
        for form in note:
            if letter.upper() == form:
                # Position in note list
                answer = i
                break
        i += 1

    # Add the octave to the above note position
    answer += (int(midstr[-1])) * 12
    # return the midinote
    return answer

def play_midi_bits(bits: list):
    """
    Uses fluidsynth to play back the list of notes in Music21 format.
    :param bits: randomised list of notes (name_octave, duration)
    """
    # Iterate through the random list of notes
    for n in bits:
        print(n)
        pitch = n[0]
        duration = n[1]

        # midi note calculation
        midi_note = calc_midi_note(pitch)

        # play the note, wait then stop
        fs.noteon(0, midi_note, 70)
        sleep(duration/2)
        fs.noteoff(0, midi_note)

def main():
    # Send a Midifile path to
    midi_bits = get_midi_bits("book1-prelude01.mid")
    # Shuffle it for fun
    shuffle(midi_bits)
    shuffled_midi_bits = midi_bits
    shuffle (shuffled_midi_bits)

    t1 = Thread(target=play_midi_bits,
                args=(midi_bits,)
                )
    t2 = Thread(target=play_midi_bits,
                args=(shuffled_midi_bits,)
                )

    t1.start()
    t2.start()
    t2.join()


#  Code starts here
if __name__ == "__main__":
    # Send a Midifile path to
    midi_bits = get_midi_bits("book1-prelude01.mid")
    # Shuffle it for fun
    shuffle(midi_bits)
    # Play the resultant new composition
    play_midi_bits(midi_bits)

# Alternative two-part version
# if __name__ == "__main__":
#     main()
