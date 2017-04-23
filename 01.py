import random
import sys
import os

words = list()
uniqueWords = list()

originalText = open('emma.txt', 'r').read()

for i in originalText.split():
	i = (i.rstrip('?:!.,;-')).lower()
	words.append(i)

for i in words:
	if i != '':
		if i not in uniqueWords:
			uniqueWords.append(i)

# The following is what actually generates the poem, using the unique words list
# created above. The first range ('0,100') is total the number of words to be used in
# the output. Change this to as long or as short as you wish. The second range
# is what actually generates the number of words per line. Play around with this,
# to get varying lengths that suit you. Have fun!

poem_raw = list()

wordsPerLine = 8

for i in range(0,1000):
	poem_raw.append(random.choice(uniqueWords))

for i in range(len(poem_raw)/wordsPerLine+1):
    print " ".join(poem_raw[i*wordsPerLine:(i+1)*wordsPerLine])
