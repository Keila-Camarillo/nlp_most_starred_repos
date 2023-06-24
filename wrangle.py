
#standard imports
import pandas as pd
import numpy as np

#parsing data
import re
import unicodedata
import nltk
from nltk.corpus import stopwords


def basic_clean(string):
    
    string = string.lower() #lowercasing
    string = unicodedata.normalize('NFKD', string).encode('ascii', 'ignore').decode('utf-8') #normalizing
    string = re.sub(r'[^a-z0-9\'\s]', '', string) #replace extra things
    
    return string

def tokenize(string):
    
    tokenize = nltk.tokenize.ToktokTokenizer() #creating the tokenize
    string = tokenize.tokenize(string, return_str=True) #using the tokenize
    
    return string


def stem(string):
    
    ps = nltk.porter.PorterStemmer() #creating my stemmer
    stems = [ps.stem(word) for word in string.split()] #splitting into each word and applying the stemmer
    string = ' '.join(stems) #joining all into one string
    
    return string

def remove_stopwords(string, extra_words=[], exclude_words=[]):
    
    stopwords_ls = stopwords.words('english') #defining my stopwords
    
    stopwords_ls = set(stopwords_ls) - set(exclude_words) #removing any stopwords in my exclude list
    stopwords_ls = stopwords_ls.union(set(extra_words)) #adding any stopwards from my extra list
    
    words = string.split() #splitting up my string
    filtered_words = [word for word in words if word not in stopwords_ls] #use listcomp to remove words in stopwords_ls
    string = ' '.join(filtered_words) #joining back to a string
    
    return string

def lemmatize(string):
    
    wnl = nltk.stem.WordNetLemmatizer() #creating my lemmatizer
    lemmas = [wnl.lemmatize(word) for word in string.split()] #splitting my string into words and applying the lemma
    string = ' '.join(lemmas) #joining back into one string

    return string

def clean_df(df, extra_words=[], exclude_words=[]):
    """
    Send in df with columns: title and original,
    returns df with original, clean, stemmed, and lemmatized data
    """
    df['clean'] = df.original\
                        .apply(basic_clean)\
                        .apply(tokenize)\
                        .apply(remove_stopwords, 
                                    extra_words=extra_words,
                                    exclude_words=exclude_words)
    df['stemmed'] = df.clean.apply(stem)
    df['lemmatized'] = df.clean.apply(lemmatize)
    
    return df