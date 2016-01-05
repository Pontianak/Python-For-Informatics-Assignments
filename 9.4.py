# Copyright (c) 2015 Pontianak

"""
9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

eMailDict = dict()
largestName = None
largestCount = None

for line in handle :
    if line.startswith("From:") : continue
    if line.startswith("From") :
        line = line.split()
        tempHandle = line[1]
        eMailDict[tempHandle] = eMailDict.get(tempHandle,0) + 1

for counter in eMailDict :
    if largestCount == None or largestCount < eMailDict[counter] :
        largestName = counter
        largestCount = eMailDict[counter]
print largestName , largestCount
