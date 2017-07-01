words = {}
with open('dataset_3363_3.txt') as inf:
	l = []
	for line in inf:
		line = line.strip()
		l = [w for w in line.lower().split()]
		for w in l:
			if w in words:
				words[w] = words.get(w) + 1
			else:
				words[w] = 1

freqWord = ''
maxCount = 0
for word, count in words.items():
	if count > maxCount:
		maxCount = count
		freqWord = word
	elif count == maxCount:
		if word < freqWord:
			freqWord = word

print(freqWord + ' ' + str(maxCount))