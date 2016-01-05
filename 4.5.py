import os

def fred():
    print "Zap"

def jane():
    print "ABC"

"""
Should print:
ABC
Zap
ABC
"""
os.system('cls')
jane()
fred()
jane()
