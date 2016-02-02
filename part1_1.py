import nltk
import math
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import gutenberg
from nltk.util import bigrams
from nltk.util import trigrams

text = gutenberg.raw('austen-emma.txt');
nltk_sents = sent_tokenize(text)						# contains the list of sentences detected from the tool
nltk_words = word_tokenize(text)
dictn=list(set(nltk_words))
tokens = nltk_words
#print type(tokens[0])
tokens = [token.lower() for token in tokens if len(token) > 1] 		# same as unigrams
bi_tokens = list(bigrams(tokens))					# getting the bigrams
tri_tokens = list(trigrams(tokens))


uni_fdist = nltk.FreqDist(tokens)
bi_fdist = nltk.FreqDist(bi_tokens)

tri_fdist = nltk.FreqDist(tri_tokens)
tri_freq = 0
uni_freq = 0
bi_freq = 0


print "top 15 unigrams\n\n"

for k,v in uni_fdist.most_common(15):
	print k,v

print "top 15 bigrams\n\n"

for k,v in bi_fdist.most_common(15):
	print k,v

print "top 15 trigrams\n\n"

for k,v in tri_fdist.most_common(15):
	print k,v


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




#print len(bi_fdist)

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


