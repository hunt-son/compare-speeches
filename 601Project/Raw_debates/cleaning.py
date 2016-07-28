from __future__ import division
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer
from stop_words import get_stop_words

stopset = set(stopwords.words('english'))
stopset2 = get_stop_words('english')
st = LancasterStemmer()

with open('dem1.txt', 'r') as text_file:
	for text in text_file:
	    
	    tokens=word_tokenize(str(text))
	    # print(tokens)
	    tokens = [st.stem(w) for w in tokens]
	    # print(tokens)
	    tokens = [w for w in tokens if not w in stopset2]
	    
	    print tokens