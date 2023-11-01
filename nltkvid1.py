import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize,word_tokenize
"""
Tokenizing - There are two kind of tokenizers
            1> Word Tokenizers- Seperates by words.
            1> Sentences Tokenizers- Seperates by sentences.

Corpora- Body of texts. eg= Medical journals, English Language, Presidental Speeches
lexion-  Words and their meanings.
"""
example_text="Hello Mr. Rohan Debnath. How are you today?"

# print(word_tokenize(example_text)) #Words into consideration.
# print()
# print(sent_tokenize(example_text)) #Sentences into consideration.

for i in word_tokenize(example_text):
    print(i,end=" ")