# Copyright (c) 2015 Pontianak

"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

tmpDict = dict()
for counter in handle :
    if counter.startswith("From") and len(counter.split()) > 2 :
        tmp = counter.split()
        if not tmpDict.has_key(tmp[5][:2]) :
            tmpDict[tmp[5][:2]] = 1
        else :
            tmpDict[tmp[5][:2]] += 1

key = sorted(tmpDict)
for counter in key :
    print counter , tmpDict[counter]
