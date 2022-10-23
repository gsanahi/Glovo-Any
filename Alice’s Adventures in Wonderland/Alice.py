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

names = ['hdb—','Annie Aa', 'Hola.', 'John Psuffixes$', ] 

suffixes = set(punctuation + "— ")

def remove_punctuation(palabra):#string ->string
    if (palabra != "") and (palabra[-1] in suffixes):
        return remove_punctuation(palabra[0:-1])
    else:
        return palabra


# def remove_apostrophe(palabra): #strig -> string
#     if palabra[-2:] == "'s":
#         return palabra[0:-2]
#     return palabra

# print(remove_apostrophe("Jorge's"))

def remove_apostrophe(palabra: str): #strig -> string
    return palabra.replace("'s","")

def remove_suffix(palabra, suffix): #string,string(sufix) -> string
    if (palabra[-len(suffix):] == suffix):
        return palabra[:-len(suffix)]
    return palabra


def normalize(lst): #List[cadenas] -> List[cadenas]
    lower = map(lambda x : x.lower(),lst)
    without_stopwords = remove_stopwords(lower,stopwords_set)
    without_punctuation = map(lambda x : remove_punctuation(x),without_stopwords)
    without_apostrophe = map(lambda x : remove_apostrophe(x),without_punctuation)
    return list(without_apostrophe)

def count_words(lst): #List -> dict
    dict = {}
    # Comprobar si esa palabra ya está en el diccionario
    for palabra in lst:
        if palabra in dict:
            # Si lo está, incrementa su valor (el contado) en una unidad
            dict[palabra] = dict[palabra] + 1
        # Si no lo está, métela con el valor de 1    
        else:
            dict[palabra] = 1
    return dict
    
#print(count_words(normalize(alice)))  


def word_probability(wordsCount):
    size = float(len(wordsCount))
    return dict(map(lambda tupla : (tupla[0],tupla[1]/size),wordsCount.items()))
    
print(word_probability(count_words(normalize(alice))))