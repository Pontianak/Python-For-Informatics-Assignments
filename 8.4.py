# Copyright (c) 2015 Pontianak

"""
8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() function. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
"""

fname = open('regex_sum_42.txt')


for line in fname:
    line = line.rstrip()
    for nums in line:
        nums = re.findall('[0-9]+',line)


nums.sum()
print nums
