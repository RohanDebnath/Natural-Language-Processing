import nltk
import random
from nltk.corpus import movie_reviews

documents = []
for category in movie_reviews.categories():
    for file_id in movie_reviews.fileids(category):
        documents.append((list(movie_reviews.words(file_id)), category))

#random.shuffle(documents)
#print(documents[0])  

all_words=[]
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words=nltk.FreqDist(all_words)
#print(all_words.most_common(10))
#print(all_words)
#print(all_words["goal"])

word_features=list(all_words.keys())[:3000]
