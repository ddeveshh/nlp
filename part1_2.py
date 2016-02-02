import nltk
import math
from nltk.corpus import gutenberg
from pattern.en import *


text = gutenberg.raw('austen-emma.txt')
#pprint(parse(text,chunks = False, tags = False).split())
pattern_words = parse(text,chunks = False, tags = False).split()
pattern_sent = tokenize(text)
#print pattern_words
tokens = pattern_words
l = []
for token in tokens:
	for i in token:
		for j in i:
			l.append(j.lower())
tokens = l
tokens = [token.lower() for token in tokens if len(token) > 1]
#dictn=list(set(tokens))
uni_tokens = ngrams(text,n = 1)
bi_tokens =  ngrams(text, n = 2)
tri_tokens =  ngrams(text, n = 3)

uni_fdist = nltk.FreqDist(uni_tokens)


uni_freq = 0

for k,v in uni_fdist.most_common():
	#print k,v
	uni_freq = uni_freq + v
x = uni_freq*(0.9)
no1 = 0
for k,v in uni_fdist.most_common():
	x = x-v
	#print k,v
	if x > 0:
		no1 = no1+1


print "for 90 percentage unigrams needed ",no1

#print x
#print uni_freq
#print len(uni_fdist)



bi_fdist = nltk.FreqDist(bi_tokens)
#print len(bi_fdist)
bi_freq = 0
for k,v in bi_fdist.most_common():
    #print k,v
    bi_freq = bi_freq + v

x = bi_freq*(0.8)
#print x
no2 = 0
for k,v in bi_fdist.most_common():
	x = x-v
	#print k,v
	if x > 0:
		no2 = no2+1

print "for 80 percentage bigrams needed ",no2

tri_fdist = nltk.FreqDist(tri_tokens)
tri_freq = 0
for k,v in tri_fdist.most_common():
	tri_freq = tri_freq + v
	#print k,v
x = tri_freq*(0.7)
no1 = 0
for k,v in tri_fdist.most_common():
	x = x-v
	#print k,v
	if x > 0:
		no1 = no1+1
		
print "for 70 percentage trigrams needed ",no1


