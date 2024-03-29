# -*- coding: utf-8 -*-
"""김주송 - HW02-Spam Filter의 사본

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RGyZXtDc1E-F4oIsXwZ4CzC79wNk786H

# HW02. Simple Naive Bayes Classifier

## T1. Load a dataset

The following code loads a dataset consisting of text messages and spam-ham labels.

You can write your own code below the **"TODOs"** to answer the questions.

### Questions:
* Number of spam messges? [*Answer here*]
* Number of ham messages? [*Answer here*]
"""

from typing import List, Tuple, Dict, Iterable, Set
from collections import defaultdict
import re
import math
import pandas as pd

url = 'https://raw.githubusercontent.com/mlee-pnu/IDS/main/spam_dataset.csv'
df = pd.read_csv(url)

# TODOs

"""## T2. Spam filter for individual words

We first defined a function ***tokenize()*** to convert a given text into a set of words.

Using the function, we now try to count the frequency of each word in each class (spam and ham).

Complete the following code and answer the following questions:

### Qeustions:
*   Number of spam messages containing the word "free": [*Answer here*]

Let's assume we only care for the word "free" to determine if a message is a spam or not. Answer the following questions:

*   P ( *ham* | *free* ) = [*Answer here*]
*   Is this message spam? [*Answer here*]

*Note: Do not apply a smoothing method here.*
"""

def tokenize(text: str) -> Set[str]:
    text = text.lower()
    all_words = re.findall("[a-z0-9']+", text)
    return set(all_words)

tokens: Set[str] = set()
token_spam_counts: Dict[str, int] = defaultdict(int)
token_ham_counts: Dict[str, int] = defaultdict(int)

spam = df[df.Category == 'spam']
ham = df[df.Category == 'ham']

for msg in spam['Message'].to_list():
  for token in tokenize(msg):
    tokens.add(token)
    token_spam_counts[token] += 1

for msg in ham['Message'].to_list():
  for token in tokenize(msg):
    tokens.add(token)
    token_ham_counts[token] += 1

# TODOs
word = "free"
n_word_spam = # frequency of the word in spam messages
n_word_ham =  # frequency of the word in ham messages

p_spam =  # P(spam)
p_ham =   # P(ham)
p_word_given_spam = # P(word|spam)
p_word_given_ham =  # P(word|ham)

# p(spam|word)
p_spam_given_word =
# P(ham|word)
p_ham_given_word =

"""## T3. Spam filter that combines words: Naive Bayes

You received a text message "just do it" from an unknown sender.

Complete the function ***predict()*** that outputs the probability of the message being spam and the predicted label of the message.

### Questions:

*   P ( *spam* | *text* ) = [*Answer here*]
*   Is this text message spam? [*Answer here*]

*Note: You do not need to apply a smoothing method here.*
"""

text = "just do it"

# TODOs
def predict(text: str):
  prob = 1
  label = "spam"
  return prob, label

print(predict(text))

"""## T4. Smoothing method

You again received two text messages from unknown senders.

Complete the function ***spamFilter()*** that classifies a given message.

You may want to apply a smoothing method for this task.

### Questions:

*   Is textA spam?: [*Answer here*]
*   Is textB spam?: [*Answer here*]
"""

textA = "reward! download your free ticket from our website www.pnu.edu"
textB = "call me and get your money back"

# TODOs
def spamFilter(text: str):
  label = "spam"
  return label

print(spamFilter(textA))
print(spamFilter(textB))