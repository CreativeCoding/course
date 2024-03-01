# Original source : https://web.mit.edu/music21/doc/testsAndInProgress/devTest_unconvertedExamples.html

# Import every module from Music21 -- not very optimised, not advised!!
from music21 import *
from random import randrange

# Parse the Bach xml file into a Music21 container for processing
src = corpus.parse('bach/bwv323.xml')

# Extract a specific element from the container (Soprano part), and seperate out into only note and rest data
soprano = src.getElementById('Soprano').recurse().notesAndRests.stream()

# Show in an external MusicXML software
# soprano.show()

# Make a blank score in Music21
outputScore = stream.Score()

# set out a few transformation parameters. List of tuples: (speed, transposition)
transformations = [((randrange(0, 300) / 100), 'P1'),
                   (2.0, '-P5'),
                   (0.5, '-P11'),
                   (1.5, -24)  # 24 semitones down
                   ]

# Iterate through each of the parameters in transformations
for speed, transposition in transformations:
    # Make a new part from the original soprano extraction
    part = soprano.augmentOrDiminish(speed)
    # Transpose
    part.transpose(transposition, inPlace=True)
    # Insert into the blank score
    outputScore.insert(0, part)

# Show in an external MusicXML software
outputScore.show()
