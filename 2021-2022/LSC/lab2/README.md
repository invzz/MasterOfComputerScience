
# Word Counter

---

using Docker compose - zookeper - kafka - confluent kafka - kafdrop

---

## Developers

Andres Coronado, Garbarino Giacomo

## Instructions

1. run `docker-compose up`
   - create topic with `kafdrop` in [http://localhost:9000]
2. run the consumer code 
   - `python consumer.py mytopic 4`
3. run the producer code
   - `python producer.py /path/to/my/text/file.txt mytopic`
