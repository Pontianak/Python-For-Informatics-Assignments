# Copyright (c) 2016 Pontianak
# Please note os.system('cls') works only on Windows systems.

import urllib, os
from BeautifulSoup import *

os.system('cls')

print 'Sample Problem: https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html'
print 'Actual Problem: https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Tymon.html'

while True:
    try:
        uInput = int(raw_input('\nEnter # Sample "1" or Actual "2"\n> '))
    except:
        print 'Error: Enter a number 1 or 2'
        continue
    if uInput == 1:
        url = 'https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html'
        cSeq = 'Sequence of names: Fikret Montgomery Mhairade Butchi Anayah\nLast name in sequence: Anayah'
        pos = 3
        repeat = 4
        break
    elif uInput == 2:
        url = 'https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Tymon.html'
        cSeq = 'The first character of the name of the last page that you will load is: E'
        pos = 18
        repeat = 7
        break
    elif uInput < 1:
        print 'Error: Invalid Entry\nEnter a number 1 or 2'
        continue
    elif uInput > 2:
        print 'Error: Invalid Entry\nEnter a number 1 or 2'
        continue

cRepeat = 0
cPos = 0

print '\nProcessing:' , url

while cRepeat < repeat:
    html = urllib.urlopen(url) .read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    for tag in tags:
        temp = tag.get('href' , None)
        cPos += 1
        if cPos == pos:
            url = temp
            cPos = 0
            cRepeat += 1
            if cRepeat < repeat:
                print 'Processing:' , url
            else:
                print 'Last URL:' , url
            break
print '\n' , cSeq
