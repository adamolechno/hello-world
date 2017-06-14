#!/usr/bin/env python
import logging
import random
import kafka

logging.basicConfig(level=logging.DEBUG,
                    filename='xxxxxx/python-kafka-produer.log',
                    format='"%(asctime).19s", "%(name)s", "%(levelname)s",'
                           '"%(message)s"')

log = logging.getLogger(__name__)


class KafkaProducer:
    '''
    Producer that creates files with random number generator.
    '''
    def __init__(self, file=None, how_many_random_numbers=None, bootstrap_servers=None, topic=None):
        self.file = file
        self.how_many_random_numbers = how_many_random_numbers
        self.bootstrap_servers = bootstrap_servers
        self.topic = topic

    def file_generator(self, file, how_many_random_numbers):
        '''
        Module that create csv file with 2 random generate number.
        '''
        i = 0
        log.info('Create file %s.' % file)
        write_to_file = open(file, 'wb')
        for i in range(how_many_random_numbers):
            random_number = random.randint(000000000, 999999999)
            random_number_two = random.randint(000000000, 999999999)
            log.info('Create random number %d and number %d' % (random_number, random_number_two))
            write_to_file.write('%d;%d\n' % (random_number, random_number_two))
            log.info('Write random numbers to file successfully!')

        log.info('Close file %s.' % file)
        write_to_file.close()
        log.warn('File %s closed.' % file)

    def kafka_producer(self, bootstrap_servers, topic):
        '''
        Create producer and push file with random generates number into brokers.
        '''

        producer = kafka.KafkaProducer(bootstrap_servers=bootstrap_servers)
        for i in range(10):
            producer.send(topic, i)

    def kafka_consumer(self, bootstrap_servers, topic):
        '''
        Sample consumer who reads data from topic.
        '''
        consumer = kafka.KafkaConsumer(topic, bootstrap_servers=bootstrap_servers)
        for msg in consumer:
            print msg


if __name__ == "__main__":
    a = KafkaProducer()
#   a.file_generator('xxxxx/filegenerator.csv', 10)
    a.kafka_producer('xxxx:6667, xxxx:6667', 'test')
    a.kafka_consumer('test', 'xxxx:6667, xxx:6667')
