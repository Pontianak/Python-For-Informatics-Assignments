# Copyright (c) 2016 Pontianak

import os

try:
    os.system('cls')
    hrs = raw_input("Enter Hours: ")
    h = float(hrs)
    rph = raw_input("Enter Rate Per Hour: ")
    r = float(rph)

    if h <= 40:
        grossPay = r * h
        os.system('cls')
        print "Hours:" , hrs
        print "Rate Per Hour:" , rph
        print "Gross Pay:" , grossPay
    elif h > 40:
        # Get the Gross Pay before above 40
        grossPay = 40 * r
        # Adjust Hours from user entered - 40 for OT
        h = h - 40
        # Adjust Rate per Hour for OT
        r = r * 1.5
        # Total Gross Pay is the previous at 40 ours + the OT Calucations (r * h)
        grossPay = grossPay + (r * h)
        os.system('cls')
        print "Hours:" , hrs
        print "Rate Per Hour:" , rph
        print "Gross Pay:" , grossPay
except:
    print "You did not enter a number! Terminating program."
