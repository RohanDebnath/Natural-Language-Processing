#Stop Words - Stop words are a set of commonly used words in a language. 
            # Examples of stop words in English are “a,” “the,” “is,” “are,” etc.
            #  Stop words are commonly used in Text Mining and Natural Language Processing (NLP) 
            # to eliminate words that are so widely used that they carry very little useful information.

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_text="This is an example of Stop word Filteration."
stop_words=set(stopwords.words("english"))
#print(stop_words) You can view all Stop Words from here

words=word_tokenize(example_text)
filtered_sentence=[]
for w in words: 
    if w not in stop_words:
        filtered_sentence.append(w) 

print(filtered_sentence)

#Illustating the same loop wala code in short format
filtered_sentenceWithoutUsingLoop=[w for w in words if not w in stop_words]
print(filtered_sentenceWithoutUsingLoop)
