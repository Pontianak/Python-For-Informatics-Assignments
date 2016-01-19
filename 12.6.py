# Copyright (c) 2016 Pontianak
# Please note os.system('cls') works only on Windows systems. 

import urllib, os
from BeautifulSoup import *

os.system('cls')
print 'Sample data: http://python-data.dr-chuck.net/comments_42.html'
print 'Actual data: http://python-data.dr-chuck.net/comments_190148.html'

while True:
    try:
        uInput = int(raw_input('\nEnter # Sample "1" or Actual "2"\n> '))
    except:
        print 'Error: Enter a number 1 or 2'
        continue
    if uInput == 1:
        url = 'http://python-data.dr-chuck.net/comments_42.html'
        oTotal = 2482
        break
    elif uInput == 2:
        url = 'http://python-data.dr-chuck.net/comments_190148.html'
        oTotal = 'Sum ends with "6"'
        break
    elif uInput < 1:
        print 'Error: Invalid Entry\nEnter a number 1 or 2'
        continue
    elif uInput > 2:
        print 'Error: Invalid Entry\nEnter a number 1 or 2'
        continue

html = urllib.urlopen(url) .read()
soup = BeautifulSoup(html)

tags = soup('span')

count = 0
total = 0

for tag in tags:
    number = re.findall('[0-9]+', str(tag))
    number = int(number[0])
    count += 1
    total += number

os.system('cls')
print 'Selected URL:' , url , '\n\nCount:' , count , '\nTotal:' , total , '\nExpected Total:' , oTotal
