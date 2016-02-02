# encoding=utf8
import nltk
import math
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import gutenberg
from nltk.stem import WordNetLemmatizer
from nltk.util import bigrams
from nltk.util import trigrams
from nltk.corpus import wordnet


def get_wordnet_pos(treebank_tag):

    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return ''

wordnet_lemmatizer = WordNetLemmatizer()

text = gutenberg.raw('austen-emma.txt');
nltk_sents = sent_tokenize(text)						# contains the list of sentences detected from the tool
nltk_words = word_tokenize(text)
print len(nltk_words)

#fnltk_words = [wordnet_lemmatizer.lemmatize(nltk_word) for nltk_word in nltk_words]
#print len(fnltk_words)
dictn=list(set(nltk_words))
tokens = nltk_words

tokens = [token.lower() for token in tokens if len(token) > 1] 		# same as unigrams
lemma_tokens = [wordnet_lemmatizer.lemmatize(token, wordnet.VERB) for token in tokens]
print len(lemma_tokens)
tokens = lemma_tokens
bi_tokens = list(bigrams(tokens))					# getting the bigrams
tri_tokens = list(trigrams(tokens))


uni_fdist = nltk.FreqDist(tokens)

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


