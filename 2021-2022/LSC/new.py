import string, sys
from collections import Counter
from string import punctuation
import nltk
from multiprocessing import Pool
from multiprocessing import Manager, current_process
import time
import os
from nltk import data




from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from functools import partial



def pool_counter_update(cdict,str):
    #upate str in cdict
    if str in cdict:
        cdict[str] +=1
    else:
        cdict[str]=1
    return

def pool_count_tokens_in_a_line(cdict, line):
    #p = current_process()
    #print (p.name)
  
    tword=word_tokenize(line.strip('\n'))
    #update cdict
    for str in tword:
        pool_counter_update(cdict, str)
    

def go(concurrent):
  pool=Pool(concurrent)
  start = time.time()
  man = Manager();
  #create a shared dict using base manager
  cdict = man.dict()
  wrk =  partial(pool_count_tokens_in_a_line, cdict)
  #submit a task to the pool using default chunksize partitioning of data
  pool.map(wrk, lines )
  end1 = time.time()
  return cdict


if __name__ == "__main__":

    #conf
    nltk.download('punkt')
    nltk.download('stopwords')
    swords = stopwords.words("english")

    #read a text file
    filename="input.txt"
    text_file = open(filename, "r")
    lines= text_file.readlines()
    text_file.close()
    nrows=len(lines)
    print(nrows)
    
    for i in range(4): 
        print(go(i+1))
