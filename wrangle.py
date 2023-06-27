
#standard imports
import pandas as pd
import numpy as np

#parsing data
import re
import unicodedata
import nltk
from nltk.corpus import stopwords
import json
from sklearn.model_selection import train_test_split

import warnings
warnings.filterwarnings('ignore')

def basic_clean(string):
    """
    Perform basic cleaning operations on the input string.
    
    Args:
        string (str): The input string to be cleaned.
        
    Returns:
        str: The cleaned string after performing the following operations:
             1. Lowercasing all characters.
             2. Normalizing the string by converting it to ASCII and removing any diacritics.
             3. Removing any characters that are not lowercase letters, digits, apostrophes, or whitespaces.
    """
    
    string = string.lower() #lowercasing
    string = unicodedata.normalize('NFKD', string).encode('ascii', 'ignore').decode('utf-8') #normalizing
    string = re.sub(r'[^a-z0-9\'\s]', '', string) #replace extra things
    
    return string

def tokenize(string):
    """
    Tokenizes a given string into individual tokens.
    
    Args:
        string (str): The input string to be tokenized.
        
    Returns:
        str: The tokenized string.
    """
    
    tokenize = nltk.tokenize.ToktokTokenizer() #creating the tokenize
    string = tokenize.tokenize(string, return_str=True) #using the tokenize
    
    return string


def stem(string):
    """
    Apply stemming to the input string using the Porter stemming algorithm.

    Args:
        string (str): The input string to be stemmed.

    Returns:
        str: The stemmed string where each word has been transformed to its root form.
    """
    
    ps = nltk.porter.PorterStemmer() #creating my stemmer
    stems = [ps.stem(word) for word in string.split()] #splitting into each word and applying the stemmer
    string = ' '.join(stems) #joining all into one string
    
    return string

def remove_stopwords(string, extra_words=[], exclude_words=[]):
    """
    Removes stopwords from a given string.

    Args:
        string (str): The input string from which stopwords need to be removed.
        extra_words (list, optional): Additional words to be considered as stopwords. Defaults to an empty list.
        exclude_words (list, optional): Words to be excluded from the stopwords list. Defaults to an empty list.

    Returns:
        str: The input string with stopwords removed.

    """
    
    stopwords_ls = stopwords.words('english') #defining my stopwords
    
    stopwords_ls = set(stopwords_ls) - set(exclude_words) #removing any stopwords in my exclude list
    stopwords_ls = stopwords_ls.union(set(extra_words)) #adding any stopwards from my extra list
    
    words = string.split() #splitting up my string
    filtered_words = [word for word in words if word not in stopwords_ls] #use listcomp to remove words in stopwords_ls
    string = ' '.join(filtered_words) #joining back to a string
    
    return string

def lemmatize(string):
    """
    Lemmatizes a given string using WordNetLemmatizer from NLTK.

    Args:
        string (str): The input string to be lemmatized.

    Returns:
        str: The lemmatized string.
    """
    
    wnl = nltk.stem.WordNetLemmatizer() #creating my lemmatizer
    lemmas = [wnl.lemmatize(word) for word in string.split()] #splitting my string into words and applying the lemma
    string = ' '.join(lemmas) #joining back into one string

    return string

def clean_df(df, extra_words=[], exclude_words=[]):
    """
    Clean and preprocess a DataFrame column.
    
    Parameters:
        - df (pandas.DataFrame): The DataFrame containing the data to be cleaned.
        - original (str): The name of the column in the DataFrame to be cleaned.
        - extra_words (list, optional): Additional words to be included in the list of stopwords. Default is an empty list.
        - exclude_words (list, optional): Words to be excluded from the list of stopwords. Default is an empty list.
        
    Returns:
        pandas.DataFrame: The cleaned DataFrame with additional columns for cleaned, stemmed, and lemmatized versions of the original column.
    """
    # dropping nulls
    df = df.dropna()
    
    # Define a list of the most common languages (hard-coded for time)
    languages = ['JavaScript', 'Objective-C', 'Java', 'Ruby', 'Python', 'Swift']

    # Change values to "other" if not in the most common languages
    df.loc[~df['language'].isin(languages), 'language'] = 'other'

    df['clean'] = df.readme_contents\
                        .apply(basic_clean)\
                        .apply(tokenize)\
                        .apply(remove_stopwords, 
                                    extra_words=extra_words,
                                    exclude_words=exclude_words)
    df['stemmed'] = df.clean.apply(stem)
    df['lemmatized'] = df.clean.apply(lemmatize)
    
    # add a column which is the length of the string in readme_contents
    df['readme_length'] = [len(content) for content in df.readme_contents]
    
    return df

def split_data(df, target_variable='language'):
    '''
    Takes in two arguments the dataframe name and the ("target_variable" - must be in string format) to stratify  and 
    return train, validate, test subset dataframes will output train, validate, and test in that order.
    '''
    train, test = train_test_split(df, #first split
                                   test_size=.2, 
                                   random_state=123, 
                                   stratify= df[target_variable])
    train, validate = train_test_split(train, #second split
                                    test_size=.25, 
                                    random_state=123, 
                                    stratify=train[target_variable])
    return train, validate, test