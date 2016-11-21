# Name_Badge_classifier
A machine learning application to classify badges using names

# What is Name_Badge_Classifier?
It is an application of a simple machine learning alogrithm called 'Naive Bayesian Classifier'.  
The goal of this appication is to classify people using their names and then badge them either with '+' or '-'.
  
# Getting started
We will start with dividing the data file into two files, the first one contains the training data we are going to train our algorithm with, and the second one will contain the testing data that will be used to gauge the accuracy of our algorithm.

* the data file has a 295 lines of data, will take 200 of them for training and the remaining for testing
using Bash:

split data file for training and testing
'''
$ head -n200 badges.data > training
$ tail -n95 badges.data > testing
'''

running the algorithm on the new data files
'''
$ python classifier.py training test
'''

# acknowledgment
the data file obtained from [UCI](https://archive.ics.uci.edu/ml/index.html)
ff
