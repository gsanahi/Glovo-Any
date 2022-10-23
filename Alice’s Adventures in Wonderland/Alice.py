from functools import reduce
from string import punctuation
from nltk.tokenize import word_tokenize
import string 


with open('./Alice’s Adventures in Wonderland/Alice.txt', 'r') as story:
    alice = word_tokenize(story.read())
    

with open('./Alice’s Adventures in Wonderland/english.txt', 'r') as datasets:
    list_of_stopwords =(datasets.read()).split()
    stopwords_set = set(list_of_stopwords)

 
def remove_stopwords(txt,wordsToRemove): #list[str], set[stopwords] -> Newlist [str]
    return list(filter(lambda x : not x in wordsToRemove, txt))

#print(remove_stopwords(alice,stopwords_set))

names = ['hdb-','Annie Aa', 'Hola.', 'John PLG$', "Piggy Alpha CLa'", "here’s"]


def remove_punctuation(txt):
    suffixes = list(string.punctuation)
    new_names = []
    for name in txt:
        for suffix in suffixes:
            if name.lower().endswith(suffix.lower()):
                name = name[:-len(suffix)]
                new_names.append(name)
    else:
        new_names.append(name)
    return new_names

#print(remove_punctuation(names))



