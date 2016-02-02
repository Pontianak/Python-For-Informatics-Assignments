# Copyright (c) 2016 Pontianak
# Please note os.system('cls') works only on Windows systems.

import urllib, os
import xml.etree.ElementTree as ET

os.system('cls')
address = raw_input('Enter location\n> ')

os.system('cls')
print 'Retrieving >', address

site = urllib.urlopen(address)
data = site.read()
print '\nRetrieved',len(data),'characters'
tree = ET.fromstring(data)

results = tree.findall('comments/comment/count')
counts = [int(itr.text) for itr in results]
tSum = sum(counts)

print 'Count:' , len(counts)
print 'Sum:' , tSum
