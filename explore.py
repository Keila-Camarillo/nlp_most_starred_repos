import nltk
import pandas as pd

import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# sklearn imports
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.feature_extraction.text import CountVectorizer

# tree classifier
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree

# rainforest classifier
from sklearn.ensemble import RandomForestClassifier

# linear regession classifier
from sklearn.linear_model import LogisticRegression

# KNN classifier
from sklearn.neighbors import KNeighborsClassifier
import wrangle as w

def make_ngram(words, n):
    return pd.Series(nltk.ngrams(words, n)).value_counts(ascending=False)

def split_data_xy(train, validate, test, target="language"):
    '''
    This function take in a dataframe performs a train, validate, test split
    Returns train, validate, test, X_train, y_train, X_validate, y_validate, X_test, y_test
    and prints out the shape of train, validate, test
    '''
    #Split into X and y
    x_train = train.lemmatized
    y_train = train[target]

    x_validate = validate.lemmatized
    y_validate = validate[target]

    x_test = test.lemmatized
    y_test = test[target]
    

    # Have function print datasets shape
    print(f'train -> {train.shape}')
    print(f'validate -> {validate.shape}')
    print(f'test -> {test.shape}')
   
    return train, validate, test, x_train, y_train, x_validate, y_validate, x_test, y_test

def get_word_viz(df):
    """
    Generates a word visualization based on the input DataFrame.

    Args:
        df (pandas.DataFrame): Input DataFrame containing language and lemmatized columns.

    Returns:
        None
    """

    # Join words from each language category into one string and split into a list of words
    java_words = ' '.join(df[df.language == 'Java'].lemmatized).split()
    javascript_words = ' '.join(df[df.language == 'JavaScript'].lemmatized).split()
    other_words = ' '.join(df[df.language == 'other'].lemmatized).split()
    swift_words = ' '.join(df[df.language == 'Swift'].lemmatized).split()
    python_words = ' '.join(df[df.language == 'Python'].lemmatized).split()
    objectivec_words = ' '.join(df[df.language == 'Objective-C'].lemmatized).split()
    ruby_words = ' '.join(df[df.language == 'Ruby'].lemmatized).split()
    all_words = ' '.join(df.lemmatized).split()

    # Get the frequency counts for each language category and all words
    java_freq = pd.Series(java_words).value_counts()
    javascript_freq = pd.Series(javascript_words).value_counts()
    other_freq = pd.Series(other_words).value_counts()
    swift_freq = pd.Series(swift_words).value_counts()
    python_freq = pd.Series(python_words).value_counts()
    objectivec_freq = pd.Series(objectivec_words).value_counts()
    ruby_freq = pd.Series(ruby_words).value_counts()
    all_freq = pd.Series(all_words).value_counts()
    
    # Combine freq series into a dataframe called word_counts
    word_counts = pd.concat([all_freq, java_freq, javascript_freq, other_freq, swift_freq,
                            python_freq, objectivec_freq, ruby_freq], axis=1, sort=True)

    # Fill NaN values with 0
    word_counts = word_counts.fillna(0)
    
    # Convert float values to integers
    word_counts = word_counts.apply(lambda s: s.astype(int))
    
    # Rename the columns
    word_counts.columns = ['all', 'java', 'javascript', 'other', 'swift', 'python', 'objective_c', 'ruby']
    
    # Create visualization
    languages = word_counts.columns[1:]
    
    # Setting basic style parameters for matplotlib
    plt.rc('figure', figsize=(13, 7))
    plt.style.use('seaborn-whitegrid')

    # Visualization of top 10 words by programming language
    word_counts.sort_values('all', ascending=False)[languages].head(10).plot.barh(title="Top 10 Words by Programming Language")



def plot_bigrams_graph():
    """
    Plots a bar graph of the most common bigrams by language.

    Returns:
        None
    """
    data = {
        ('plugged', 'app'): 9, 
        ('npm', 'install'): 29,
        ('written', 'rust'): 43,
        ('structured', 'concurrency'): 7,
        ('info', 'address'): 5,
        ('status', 'bar'): 12,
        ('include', 'hermodel'): 37
    }

    # Extract the labels and counts from the data dictionary
    labels = [f"{word1}, {word2}" for (word1, word2) in data.keys()]
    counts = list(data.values())

    # Define colors for each bar graph
    colors = ['#FFC0CB', '#FFA07A', '#FFA500', '#FFD700', '#ADFF2F', 'cyan', '#E6E6FA']

    # Plotting the bar graph
    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, counts)

    # Set different colors for each bar
    for i, bar in enumerate(bars):
        bar.set_color(colors[i])

    plt.xlabel('Bigram')
    plt.ylabel('Count')
    plt.title('Most Common Bigram by Language')

    # Create a legend for the colors
    legend_labels = ['Java', 'JavaScript', 'Other', 'Swift', 'Python', 'Objective-C', 'Ruby']
    legend_colors = [plt.Rectangle((0, 0), 1, 1, color=color) for color in colors]
    plt.legend(legend_colors, legend_labels)

    # Rotate the x-axis labels for better visibility
    plt.xticks(rotation=45, ha='right')

    # Remove gridlines
    plt.grid(False)

    # Display the plot
    plt.show()
