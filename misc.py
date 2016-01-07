import os

os.system('cls')

largest = None

print "Before:" , largest , "\n"

for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest:
        largest = itervar
    print "Loop:" , itervar , largest

print '\nLargest:' , largest
