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
tokens = [token.lower() for token in tokens if len(token) > 1] 		# same as unigrams
bi_tokens = list(bigrams(tokens))					# getting the bigrams
tri_tokens = list(trigrams(tokens))




fdist = nltk.FreqDist(bi_tokens)
t = fdist1.most_common(10)
for k,v in t.items():
    print k,v


for k,v in fdist.most_common():
    print k,v


