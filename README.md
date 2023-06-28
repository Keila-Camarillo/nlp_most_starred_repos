# Programming Language Prediction Project
 
# Project Description
 
For this project, we will be using text data from >= 100 GitHub repository README files to predict the main programming language of the repository (e.g. python, java, C++, etc.). This is a Natural Language Processing (NLP) classification project.

# Presentation Slides
Click [here](https://docs.google.com/presentation/d/1rCLXl60FxKvjrrH8RpA5JjgofPzZ3D8DuX7IoykqDh4/edit?usp=drive_link) for a slideshow presentation.
 
# Project Goal
 
* Discover README features that indicate the repository programming language
* Use features to develop a machine learning model to predict the repository's main programming language
 
# Initial Thoughts
 
Our initial hypothesis is that there will be some unique words found in README files that can help identify the main programming language.
 
# The Plan
 
* Acquire a corpus of GitHub repository README files via GitHub API. Our data comes from the top 100 most-starred repositories on GitHub current as of 27 Jun 2023.
 
* Prepare data
    * Clean text by making all text lowercase, removing special characters, tokenizing the words into discrete units, and lemmatizing them to get word roots
 
* Explore data in search of drivers of upsets
   * Answer the following initial questions
       1. What are the most common words in READMEs?
       2. Does the length of the README vary by programming language?
       3. Are there any words that uniquely identify a programming language?
       4. Are there bigrams or n-grams that can uniquely identify a programming language?
      
* Develop a Model to predict the main programming language of each README
   * Use drivers identified in explore to build predictive models of different types
   * Evaluate models on train and validate data
   * Select the best model based on highest accuracy
   * Evaluate the best model on test data
 
* Draw conclusions
 
# Data Dictionary

| Feature Name | Data Type | Description | Example |
| ----- | ----- | ----- | ----- |
| repo | object | Name of Repository | 'spolu/breach_core' |
| language | object | Predominant coding language of Repository | 'JavaScript' |
| readme_contents | object | Contents of Repository's README file | '### Breach: A Browser for the HTML5 Era...' |
| lemmatized | object | Cleaned version of contents of Repository's README file | 'breach browser html5 era modular everything...' |
| readme_length | integer | number of characters in the README file | 1069 |

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
4) In the command line, run 'python acquire.py'. This will scrape the web pages and write the data to 'data.json'
4) Run final_report notebook and/or desired files

IF YOU WANT TO USE THE SAME DATA ACQUIRED ON 27 JUN 2023
1) Clone this repo
2) Download data.json from [here](https://drive.google.com/file/d/1s9NI0dd4p-ziazLXJvpTP8j0FlctR2Zp/view?usp=sharing)
3) Run final_report notebook and/or desired files

# Takeaways and Conclusions
* The most popular languages in our dataset were JavaScript, Objective-C, and Java
* There were 19 different languages in our dataset, 6 of which occurred only once, and 4 only twice
* The length of the readme did not correlate to the type of language
* There were some words and word combinations that correlated with the programming language.
    - For example, README's where Ruby was the main programming language were much more likely to have 'ruby', 'end', and 'order.  Where Swift was the main language, 'true' and 'type' appeared much more often.
 
# Conclusion and Recommendations
* Our best model was a Decision Tree model. The baseline was 27% (guessing 'JavaScript' for every entry would have been correct 27% of the time), and our best model achieved a 63% accuracy on the test data set. This is the expected accuracy on unseen data.
* With more time, we would acquire more README files to have a larger data set. We would also explore other models such as the various Naive Bayes models, to see if we could improve the accuracy.

