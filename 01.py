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
		
print(uniqueWords)
