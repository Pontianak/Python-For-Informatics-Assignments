# Copyright (c) 2015 Pontianak

"""
 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:

X-DSPAM-Confidence:    0.8475

Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.

You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
"""

count = 0
result = 0.0

# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    if line.startswith("X-DSPAM-Confidence:") :
        count = count + 1
        getNum = line.find('0')
        result = result + float(line[getNum:])
        continue
    print line
print "Average spam confidence:" , result / count
