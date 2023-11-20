from music21 import converter

# define the function
def get_midi_lists(mf: str) -> list:
    """Takes a path to a midifile, converts to Music21 stream
    then parses the metadata for each note, rest and chord into
    neoscore-ready format:
    [[pitch list: neoscore notes], duration as quarter note]

    returns: list"""

    # convert it to music21 format
    score_in = converter.parseFile(mf)

    # make a blank list
    components = []

    # parse through the midi file and extract only notes, rests, chords
    for msg in score_in.recurse().notesAndRests:

        # if note length is not 0 then convert to neoscore
        if msg.duration.quarterLength != 0:

            try:
                type = msg.name
            except:
                type = msg.pitchedCommonName

            # parse all note metadata and add to list
            try:
                pitchlist = msg.pitches
                temp_pitch_list = []

                # pitch info is a sub list of tuples (note name, octave)
                for pitch in pitchlist:
                    neopitch = pitch.name.lower()
                    neooctave = pitch.octave

                    if neopitch[-1] == "#":
                        neopitch = f"{neopitch[0]}s"
                    elif neopitch[-1] == "-":
                        neopitch = f"{neopitch[0]}f"

                    # check octave in range and add octave indicator
                    # if octave out of range then make it middle C octave
                    if 2 <= neooctave <= 6:

                        # add higher octave indicators "'"
                        if neooctave > 4:
                            ticks = neooctave - 4
                            for tick in range(ticks):
                                neopitch += "'"

                        # add lower octave indicators ","
                        elif neooctave < 4:
                            if neooctave == 3:
                                neopitch += ","
                            elif neooctave == 2:
                                neopitch += ",,"

                    # add result to ongoing list
                    temp_pitch_list.append(neopitch)

                # add all details to component list
                components.append([type, temp_pitch_list, msg.duration.quarterLength]) #, msg.pitch.name, msg.pitch.octave, msg.duration.quarterLength)

            # in case of error
            except:
                print("error:", msg)

    return components

if __name__ == "__main__":
    component_list = get_midi_lists("A Sleepin' Bee.mid")
    for c in component_list:
        print(c)