# Import python modules
from music21 import *

# Parse an xml file of Bach music into a Music21 format
bach_score = corpus.parse('bach/bwv65.2.xml')

# Analyse and print the key signature for this score
key_analysis = bach_score.analyze('key')
print(f"The key is {key_analysis}")

# Iterate through the elements contained in the file
for element in bach_score:
    print(element)
    try:
        for ele in element:
            print(ele)
            # for e in ele:
            #     print("           ", e)
    except:
        print(f"{element} is not iterable")

# Optional print xml file to MusicXML reader such as MuseScore
bach_score.show()

print("hello world")
