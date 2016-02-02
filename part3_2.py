import nltk
from nltk.corpus import gutenberg
from nltk.probability import FreqDist
from nltk.util import ngrams
from nltk import sent_tokenize, word_tokenize
from operator import itemgetter

text = gutenberg.raw('chesterton-thursday.txt')
nltk_sents = sent_tokenize(text)						# contains the list of sentences detected from the tool
nltk_words = word_tokenize(text)
tokens = nltk_words
uni_freq = FreqDist(tokens)
x = FreqDist()
y = FreqDist()
Bigram_count = 0
for line in nltk_sents:
	w = word_tokenize(line)
	for window in ngrams(w,3,pad_right=True):
		p = window[0]
		if p is None:
			continue
		for p1 in window[1:]:
			if p1 is not None:
				Bigram_count = Bigram_count +1
				x[p,p1] = x[p,p1]+1
				y[p] = y[p]+1
				y[p1] = y[p1]+1 

ct = 0
coll = []
for k,v in x.items():
	a = float(v)
	b = float(y[k[0]] - v)
	c = float(y[k[1]] - v)
	d = float(Bigram_count - y[k[0]] - y[k[1]] + v)
	z = (Bigram_count*((a*d - b*c)**2))/((a+b)*(a+c)*(b+d)*(b+c))
	if z >= 3.841:
		ct = ct +1
		coll.append([k[0],k[1],z])

coll = sorted(coll,key = itemgetter(2), reverse = True)
f= open('ans.txt','w')
for item in coll:
	item[2]=str(item[2])
	f.write(" ".join(item))
	f.write("\n")