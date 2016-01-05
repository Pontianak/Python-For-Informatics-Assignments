# Copyright (c) 2016 Pontianak

import re
import itertools

# Sums a list
def listsum(numList):
    theSum = 0
    for numTemp in numList:
        theSum = theSum + numTemp
    return theSum

assTxt = open('regex_sum_190143.txt')

numsLst = list()

# Extract numbers and put into list, remove blanks []
for line in assTxt:
    line = line.rstrip()
    temp = re.findall('[0-9]+',line)
    numsLst.append(temp)
    if temp == [] in numsLst:
        numsLst.remove(temp)

# Convert list of strings to ints
numsLst = [map(int,i) for i in numsLst]
print "\nnumsLst Output:\n"  ,  numsLst , "\n\n"

# Changes the lists in the list into 1 list
merged = list(itertools.chain(*numsLst))
print "numsLst Merged:\n" , merged , "\n\n"

print "Sum of regex_sum_190143.txt:" , listsum(merged)
