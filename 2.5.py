# Copyright (c) 2016 Pontianak

import os

os.system('cls')
cel = raw_input("What is the temp in Celsius?")

convert = float(cel) * 9
convert = convert / 5
fahr = convert + 32

os.system('cls')
print cel , "Celsius"
print fahr , "Fahrenheit"
