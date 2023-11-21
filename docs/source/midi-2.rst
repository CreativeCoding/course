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
use file midi-music21-2.py


https://www.mfiles.co.uk/downloads/book1-prelude01.mid
