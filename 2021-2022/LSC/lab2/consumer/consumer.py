# Andres        Coronado    2761046
# Garbarino     Giacomo     4545532

# usage 

# Count words!

# positional arguments:
#   Topic       topic
#   Nprocesses  parallel processes

# optional arguments:
#   -h, --help  show this help message and exit

from kafka import KafkaConsumer
import argparse
from multiprocessing import Pool
from multiprocessing import Manager

printed = False

def pool_counter_update(cdict,word):
    #upate str in cdict
    if word in cdict:
        cdict[word] +=1
        print (f"!!ADD!! -> {word} : {cdict[word]}")
       
    else:
        cdict[word]=1
        print (f"!!NEW!! -> {word} : {cdict[word]}")
    return


def word_count_worker(cdict, topic):
    
    encoding = 'utf-8'

    # To consume latest messages and auto-commit offsets
    c = KafkaConsumer(topic,
                      
                         group_id='my-group',
                         bootstrap_servers=['localhost:9092'])
    
    for m in c:
        print(f"message: {m}")
        word = m.value.decode(encoding)
        pool_counter_update(cdict,  word)
        if len( word ) == 0 and not printed : 
            printed = not printed
            print(cdict)    
        # message value and key are raw bytes -- decode if necessary!
        # e.g., for unicode: `message.value.decode('utf-8')`
        
if __name__ ==  '__main__': 
    parser = argparse.ArgumentParser(description='Count words!')
    parser.add_argument('topic', metavar='Topic', help='topic')
    parser.add_argument('numprocs', metavar='Nprocesses', help='parallel processes', type=int)
    a = parser.parse_args()  
  
   
    pool = Pool(a.numprocs)
    man = Manager()
    cdict = man.dict()
    pool.map(word_count_worker(cdict, a.topic))
    
    
  

  



