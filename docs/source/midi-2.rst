MIDI 2
======

*music21*
---------
In this lesson we will explore the *music21* library. *Music21* is a set of tools for
Computer-Aided Musical Analysis and Computational Musicology. It is possible to use
*music21* for many different purposes but in this lesson we will focus on
parsing and manipulating midifiles

Get music21
^^^^^^^^^^^
In your IDE you will need to import the *music21* library::

    pip install music21

More details of importing can be found here https://web.mit.edu/music21/doc/usersGuide/usersGuide_01_installing.html

1. *Hello music21*
^^^^^^^^^^^^^^^^^^
Use file midi-music21-1.py

Import python modules::

    from music21 import *

Parse an xml file of Bach music into a Music21 format::

    bach_score = corpus.parse('bach/bwv65.2.xml')

Analyse and print the key signature for this score::

    key_analysis = bach_score.analyze('key')
    print(f"The key is {key_analysis}")

Iterate through the elements contained in the file::

    for element in bach_score:
        print(element)
        try:
            for ele in element:
                print(ele)
        except:
            print(f"{element} is not iterable")

Optional print xml file to MusicXML reader such as MuseScore::

    bach_score.show()

2. Music21 creative experiment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In this exercise we will extract all the midi note information from a famous piece of Bach
rearrange the sequence with a random shuffle and playback the resulting composition.

First download the Bach midifile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
https://www.mfiles.co.uk/downloads/book1-prelude01.mid

Open a new python file in your IDE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Write the following or use file midi-music21-2.py

Import Python modules::

    from music21 import converter
    from random import shuffle
    import fluidsynth
    from time import sleep

Activate (instantiate) the fluidsynth object in python::

    fs = fluidsynth.Synth()
    fs.start()  # you may need to use 'start(driver=dsound)' driver in Windows or 'start(driver=alsa)' in linux

Locate the sf2 file and load into the fluidsynth object::

    sfid = fs.sfload(r'GeneralUser GS v1.471.sf2')  # replace path as needed

Select a church organ to make the sound::

    fs.program_select(0, sfid, 0, 19)

Define a function that will convert a midifile to Music21 stream
then parses the metadata for each note, rest and chord into a list::

    def get_midi_bits(mf) -> list:
        """
        Takes a path to a midifile,

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

Define another function that uses fluidsynth to play back the list of notes in
Music21 format::

    def play_midi_bits(bits: list):

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

Define a function that calculates the midi number for a given Music21 notes string, format pitch_octave.::
Taken directly from:
https://stackoverflow.com/questions/13926280/musical-note-string-c-4-f-3-etc-to-midi-note-value-in-python ::

    def calc_midi_note(midstr: str) -> int:

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

The code will start from here::

    if __name__ == "__main__":
        # Send a Midifile path to
        midi_bits = get_midi_bits("book1-prelude01.mid")
        # Shuffle it for fun
        shuffle(midi_bits)
        # Play the resultant new composition
        play_midi_bits(midi_bits)

3.1 Music21 API exploration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This code extract taken directly from the *music21* website will extract the Soprano part from a piece of Bach,
transform this part with speed changes and transposition, then rebuild a new 4 part harmony piece.

Original source : https://web.mit.edu/music21/doc/testsAndInProgress/devTest_unconvertedExamples.html

Open a new python file in your IDE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Write the following or use file midi-music21-3-1.py

Import every module from Music21 -- not very optimised, not advised!! ::

    from music21 import *

Parse the Bach xml file into a Music21 container for processing::

    src = corpus.parse('bach/bwv323.xml')

#Extract a specific element from the container (Soprano part), and separate out into only note and rest data::

    soprano = src.getElementById('Soprano').recurse().notesAndRests.stream()

Optional - show in an external MusicXML software::

    # soprano.show()

Make a blank score in Music21::

    outputScore = stream.Score()

Set out a few transformation parameters. List of tuples: (speed, transposition)::

    transformations = [(1.0, 'P1'),
                   (2.0, '-P5'),
                   (0.5, '-P11'),
                   (1.5, -24)  # 24 semitones down
                   ]

#Iterate through each of the parameters in transformations::

    for speed, transposition in transformations:
        # Make a new part from the original soprano extraction
        part = soprano.augmentOrDiminish(speed)
        # Transpose
        part.transpose(transposition, inPlace=True)
        # Insert into the blank score
        outputScore.insert(0, part)

Show in an external MusicXML software::

    outputScore.show()

3.2 Music21 API exploration part 2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This code extract taken directly from the *music21* website analyse each interval is a
corpus of Chinese traditional musics and calculate how many intervals are sevenths. It will report
these findings in the console.

Original source : https://web.mit.edu/music21/doc/testsAndInProgress/devTest_unconvertedExamples.html

Open a new python file in your IDE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Write the following or use file midi-music21-3-2.py

# Original source : https://web.mit.edu/music21/doc/testsAndInProgress/devTest_unconvertedExamples.html

Import every module from Music21 -- not very optimised, not advised!! ::

    from music21 import *

Get an analysis tool::

    diversityTool = analysis.discrete.MelodicIntervalDiversity()

Get a list to store results::

    results = []

Iterate over two specified regions in China (listed in the corpus)::

    for region in ('shanxi', 'fujian'):
        # Create storage units
        intervalDict = {}
        workCount = 0
        intervalCount = 0
        seventhCount = 0

Perform a location search on the corpus and iterate over resulting file name and work number::

    for result in corpus.search(region, field='locale'):
        workCount += 1

        # Parse the work and create a dictionary of intervals
        s = result.parse()
        intervalDict = diversityTool.countMelodicIntervals(s, found=intervalDict)

Iterate through all intervals, and count totals and sevenths::

    for label in intervalDict.keys():
        intervalCount += intervalDict[label][1]
        if label in ['m7', 'M7']:
            seventhCount += intervalDict[label][1]

Calculate a percentage and store results::

    pcentSevenths = round((seventhCount / float(intervalCount) * 100), 4)
    results.append((region, pcentSevenths, intervalCount, workCount))

Print results in the console::

    for region, pcentSevenths, intervalCount, workCount in results:
        print(f'locale: {region}: found {pcentSevenths} percent melodic sevenths '
              f'out of {intervalCount} intervals in {workCount} works')
