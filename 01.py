import random
import sys
import os

words = list()
uniqueWords = list()

originalText = open('gettysburg.txt', 'r').read()

for i in originalText.split():
	i = (i.rstrip('?:!.,;-')).lower()
	words.append(i)

for i in words:
	if i != '':
		if i not in uniqueWords:
			uniqueWords.append(i)

# uniqueWords.sort()
#
# print(uniqueWords)

poem_raw = list()
for i in range(0,100):
	poem_raw.append(random.choice(uniqueWords))

# print(poem_raw)


for i in range(len(poem_raw)/5+1):
    print " ".join(poem_raw[i*5:(i+1)*5])
