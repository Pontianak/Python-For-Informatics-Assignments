# Copyright (c) 2015 Pontianak

import os

def computegrade(Score):
    if Score < 0:
        sScore = "Bad Score"
        return sScore
    elif Score < 0.6:
        sScore = "F"
        return sScore
    elif Score > 1.0:
        sScore = "Bad Score"
        return sScore
    elif Score >= 0.9:
        sScore = "A"
        return sScore
    elif Score >= 0.8:
        sScore = "B"
        return sScore
    elif Score >= 0.7:
        sScore = "C"
        return sScore
    elif Score >= 0.6:
        sScore = "D"
        return sScore

try:
    os.system('cls')
    Score = float(raw_input("Enter Score between 0.0 and 1.0: "))
except:
    print "Bad Score"
    quit()

stringGrade = computegrade(Score)
print stringGrade
