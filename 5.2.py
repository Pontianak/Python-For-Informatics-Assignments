# Copyright (c) 2015 Pontianak

"""
Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter the numbers from the book for problem 5.1 and Match the desired output as shown.
"""

largest = None
smallest = None
count = 1
temp = None
numTest1 = None
numTest2 = None

while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break
    try:
        int(num)
    except:
        print "Invalid input"
        continue
    temp = num
    if count == 1:
        numTest1 = temp
        count  = count + 1
    else:
        numTest2 = temp
    if numTest1 > numTest2:
        largest = numTest1
        smallest = numTest2
    else:
        largest = numTest2
        smallest = numTest1

print "Maximum is", largest
print "Minimum is", smallest
