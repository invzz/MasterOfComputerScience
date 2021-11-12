
import string, sys
from collections import Counter
from string import punctuation
import nltk
from multiprocessing import Pool
import time
import os
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

swords = stopwords.words("english")

#read a text file

filename="input.txt"
text_file = open(filename, "r")
lines= text_file.readlines()
text_file.close()
nrows=len(lines)
print(nrows)



def pool_counter_update(cdict, str):

#upate str in cdict

#...



# def pool_count_tokens_in_a_line(cdict,line):

# tword=word_tokenize(line)

# #update cdict

# #...

# def go(concurrent):

#   pool=Pool(concurrent)
#   start = time.time()
#   #create a shared dict using base manager
#   #...
#   #submit a task to the pool using default chunksize partitioning of data
#   #...
#    end1 = time.time()
#    print("\nConcurrent: ",concurrent,"\nP1", end1-start)

# for i in range(4): 
#   go(i+1)