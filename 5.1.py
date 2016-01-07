# Copyright (c) 2016 Pontianak

import os

total = 0
count = 0

os.system('cls')
print 'Enter a number. Enter "done" to terminate program.\n'

while True:
    userInput = raw_input('>')
    if userInput == "done": # Calculate stuff and terminate program
        break
    try: # Invalid input catcher. Reprompts for next number.
        num = float(userInput)
    except:
        print "Error: Letter/s entered!"
        continue
    total += num
    count += 1

if total == 0:
    print "\nNothing to calculate. Program Terminated!"
else:
    avg = total / count
    print "\nTotal:" , total , "Count:" , count , "Average:" , avg
