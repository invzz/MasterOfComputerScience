import string, sys
from collections import Counter
from string import punctuation
import nltk
from multiprocessing import Pool, Manager, Process
import time
import os
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
swords = stopwords.words("english")

#read a text file
filename=r"input.txt"
text_file = open(filename, "r")
lines= text_file.readlines()
text_file.close()
nrows=len(lines)
print(nrows)


#upsert function
def pool_counter_update(cdict, str):
    if str in cdict:
        print("update")
        cdict[str] += 1
    else:
        print("insert")
        cdict[str] = 1;
    print(cdict) 


def pool_count_tokens_in_a_line(cdict,line):
  tokens = word_tokenize(line)
  return tokens; 
        
def update(cdict, lines):
  for line in lines:
    tokens = pool_count_tokens_in_a_line(cdict, lines)
    for token in tokens:
       pool_counter_update(cdict, token)
  return    

def go(concurrent):
    pool = Pool(concurrent)
    start = time.time()
    manager = Manager()
    d = manager.dict()
    #pool.map(pool_counter, d)
    pool.map(pool_count_tokens_in_a_line,[(d, lines)], 4)
    endl = time.time()
    print("\nConcurrent: ", concurrent, "\nP1", endl-start)
    end2 = time.time()
    print("P2", end2-start)
    print("-----------\n\n")
if __name__ == '__main__':
    for i in range(4):
        go(i+1)
        time.sleep(0.5)