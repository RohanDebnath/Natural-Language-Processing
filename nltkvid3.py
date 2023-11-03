#Stemming -Stemming is the process of producing morphological variants of a root/base word. 
#          Stemming programs are commonly referred to as stemming algorithms or stemmers. 
#          A stemming algorithm reduces the words “chocolates”, “chocolatey”, and “choco” 
#          to the root word, “chocolate” and “retrieval”, “retrieved”, “retrieves” reduce 
#          to the stem “retrieve”.
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps=PorterStemmer()
example_text=["Pythoner","Pythoning","Python","Pythoned","Pythonly"]

for w in example_text:
    print(ps.stem(w))

new_text="It is very important to be pythonly while you are pythoning with python. All pythoners have pythoned poorly atleast once"
words=word_tokenize(new_text)

for w in words:
    print(ps.stem(w),end=" ")
