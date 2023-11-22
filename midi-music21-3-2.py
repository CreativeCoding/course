# Original source : https://web.mit.edu/music21/doc/testsAndInProgress/devTest_unconvertedExamples.html

# Import every module from Music21 -- not very optimised, not advised!!
from music21 import *

# Get an analysis tool
diversityTool = analysis.discrete.MelodicIntervalDiversity()

# get a list to store results.
results = []

# Iterate over two regions
for region in ('shanxi', 'fujian'):
    # Create storage units
    intervalDict = {}
    workCount = 0
    intervalCount = 0
    seventhCount = 0

    # Perform a location search on the corpus and iterate over
    # resulting file name and work number
    for result in corpus.search(region, field='locale'):
        workCount += 1

        # Parse the work and create a dictionary of intervals
        s = result.parse()
        intervalDict = diversityTool.countMelodicIntervals(s, found=intervalDict)

    # Iterate through all intervals, and count totals and sevenths
    for label in intervalDict.keys():
        intervalCount += intervalDict[label][1]
        if label in ['m7', 'M7']:
            seventhCount += intervalDict[label][1]

    # Calculate a percentage and store results
    pcentSevenths = round((seventhCount / float(intervalCount) * 100), 4)
    results.append((region, pcentSevenths, intervalCount, workCount))

    # print results
    for region, pcentSevenths, intervalCount, workCount in results:
        print(f'locale: {region}: found {pcentSevenths} percent melodic sevenths '
              f'out of {intervalCount} intervals in {workCount} works')
