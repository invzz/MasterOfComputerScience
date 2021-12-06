# Andres        Coronado    2761046
# Garbarino     Giacomo     4545532

#usage 

# usage: producer.py [-h] Filename Topic

# Produce data from file.

# positional arguments:
#   Filename    filename
#   Topic       topic

# optional arguments:
#   -h, --help  show this help message and exit

from confluent_kafka import Producer
import sys
import argparse
import re


def delivery_callback(err, msg):
        if err:
            sys.stderr.write('Message failed delivery: %s\n' % err)
        else:
            sys.stderr.write(f'Message delivered to {msg.topic()} : [{msg.partition()} ] : {msg.offset()}\n')


def produce(bookname, topic) :
  
    encoding='utf-8'
    p = Producer({
    'bootstrap.servers': 'localhost:9091'
    })
    
    with open(bookname,"r",encoding=encoding) as FILE:
        for line in FILE.readlines():
            # clean
            words = re.split(r"[^A-Za-z]", line.strip())
            for word in words:
                if (word != "\n"):
                    try:
                        if len(word) > 0 :
                        # Produce words
                            p.produce(topic, word, callback=delivery_callback)
                    except BufferError:
                        sys.stderr.write('%% Local producer queue is full (%d messages awaiting delivery): try again\n' %
                                        len(p))
                    # Serve delivery callback queue.
                    # NOTE: Since produce() is an asynchronous API this poll() call
                    #       will most likely not serve the delivery callback for the
                    #       last produce()d message.
                    p.poll(0)
        # Wait until all messages have been delivered
        sys.stderr.write('%% Waiting for %d deliveries\n' % len(p))
        p.flush
     


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Produce data from file.')
    parser.add_argument('filename', metavar='Filename', help='filename')
    parser.add_argument('topic', metavar='Topic', help='topic')
    a = parser.parse_args()  
    produce(a.filename, a.topic)
    
