# Programming Language Prediction Project
 
# Project Description
 
For this project, we will be using text data from >= 100 GitHub repository README files to predict the main programming language of the repository (e.g. python, java, C++, etc.). This is a Natural Language Processing (NLP) classification project.
 
# Project Goal
 
* Discover README features that indicate the repository programming language
* Use features to develop a machine learning model to predict the repository's main programming language
 
# Initial Thoughts
 
Our initial hypothesis is that there will be some unique words found in README files that can help identify the main programming language.
 
# The Plan
 
* Aquire a corpus of GitHub repository README files via GitHub API. Our data comes from the top 100 most-starred repositories on GitHub current as of 27 Jun 2023.
 
* Prepare data
    * Clean text by making all text lowercase, removing special characters, tokenizing the words into discrete units, and lemmatizing them to get word roots
 
* Explore data in search of drivers of upsets
   * Answer the following initial questions
       * What are the most common words in READMEs?
       * Does the length of the README vary by programming language?
       * Do different programming languages use a different number of unique worrds?
       * Are there any words that uniquely identify a programming language?
       * Are there bigrams or n-grams that can uniquely identify a programming language?
      
* Develop a Model to predict the main programming language of each README
   * Use drivers identified in explore to build predictive models of different types
   * Evaluate models on train and validate data
   * Select the best model based on highest accuracy
   * Evaluate the best model on test data
 
* Draw conclusions
 
# Data Dictionary

| Feature Name | Data Type | Description | Example |
| ----- | ----- | ----- | ----- |
| repo | object | Name of Repository | 'huggingface/transformers' |
| language | object | Predominant coding language of Repository | 'Python' |
| readme_contents | object | Contents of Repository's README file | 'Transformers provides thousands of pretrained...' |
| cleaned_readme_contents | object | Cleaned version  of contents of Repository's README file | 'transformers provides thousands pretrained...' |

# Steps to Reproduce
IF YOU WANT TO SCRAPE YOUR OWN DATA:
1) Clone this repo
2) Generate a GitHub Token
    * Go here: https://github.com/settings/tokens
    * Click: 'Generate New Token(Classic)'
    * DO NOT check any boxes
    * Copy TOKEN
3) Create 'env.py' file with
    * github_username = YOUR GITHUB USERNAME
    * github_token = YOUR TOKEN
4) Run final_report notebook and/or desired files
 
# Takeaways and Conclusions
* Takeaway 1
* Takeaway 2...
 
# Recommendations
* Rec 1
* Rec 2 ...