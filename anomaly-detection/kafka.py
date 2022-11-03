from confluent_kafka import Consumer, Producer
from confluent_kafka.admin import AdminClient, NewTopic, NewPartitions
from uuid import uuid4
import json
import threading

class admin_client():
    def __init__(self, host_broker, port_broker):
        self.admin_client_istance = AdminClient({'bootstrap.servers': host_broker + ":" + port_broker})

    def create_topics(self, topicNames, n_partitions, replica):
        new_topics = [NewTopic(topic, num_partitions=n_partitions, replication_factor=replica) for topic in topicNames]
        fs = self.admin_client_istance.create_topics(new_topics)
        
        for topic, f in fs.items():
            try:
                f.result() 
                print("[adminclient]: Topic {} created".format(topic))
            except Exception as e:
                print("[adminclient]: Failed to create topic {} (maybe already exists)".format(topic))
            

    def delete_topics(self, topics):
        # Returns a dict of <topic,future>.
        fs = self.admin_client_istance.delete_topics(topics, operation_timeout=30)

        # Wait for operation to finish.
        for topic, f in fs.items():
            try:
                f.result()  # The result itself is None
                print("[adminclient]: Topic {} deleted".format(topic))
            except Exception as e:
                print("[adminclient]: Failed to delete topic {}: {}".format(topic, e))
                
    def create_partitions(a, topics):
        new_parts = [NewPartitions(topic, int(new_total_count)) for
                    topic, new_total_count in zip(topics[0::2], topics[1::2])]

        # Try switching validate_only to True to only validate the operation
        # on the broker but not actually perform it.
        fs = a.create_partitions(new_parts, validate_only=False)

        # Wait for operation to finish.
        for topic, f in fs.items():
            try:
                f.result()  # The result itself is None
                print("[adminclient]: Additional partitions created for topic {}".format(topic))
            except Exception as e:
                print("[adminclient]: Failed to add partitions to topic {}: {}".format(topic, e))

class consumer_client():
    def __init__(self, config, topic_to_subscribe):
        self.client_consumer = Consumer(config)
        self.client_consumer.subscribe(topic_to_subscribe)
    
    def consume_forever(self, queue_coords):
        time_to_wait = 2
        print("[consumer]: started to consume...   " + str(threading.current_thread().name) )
        
        while True:
            try: 
                msg = self.client_consumer.poll(timeout = time_to_wait) # la chiamata non è bloccante
                
                if msg is None:
                    continue # ogni time_to_wait secondi ripete il while
                if msg.error():
                    print("[consumer]: error happened: {}".format(msg.error()))
                    continue
                
                #print("[consumer]: Connected to Topic: {} and Partition : {}".format(msg.topic(), msg.partition()))
                #print("[consumer]: Received Message : {} with Offset : {}".format(msgClass.msg_recv, msg.offset()))
                
                consumed = msg.value().decode()
                js = json.loads(consumed)
                if len(js["People"]) > 0:
                    queue_coords.put(consumed)
                else:
                    print("[consumer]: frame " + str(js["ID_Frame"]) + " ignored.")
                
            except KeyboardInterrupt: 
                print("[consumer]: keyboardInterrupt. CONSUMER STOPPED!")
                self.client_consumer.close()
                break
            
class producer_client():
    def __init__(self, config):
        self.client_producer = Producer(config)
    
    def delivery_report(self, errmsg, msg):
        if errmsg is not None:
            print("[producer]: Delivery failed for Message: {} : {}".format(msg.key(), errmsg))
            return
        #print('[producer]: Message: {} successfully produced to Topic: {} Partition: [{}] at offset {}'.format(
        #   msg.value(), msg.topic(), msg.partition(), msg.offset()))
    
        
    def produce_forever(self, topic_to_use, queue_coords_anomaly):
        print("[producer]: ready to produce... " + str(threading.current_thread().name) )
        while(True):
            self.produce_msg(topic_to_use, queue_coords_anomaly.get())

            
    def produce_msg(self,topic_to_use, str_to_send):
        
        self.client_producer.poll(0) #serve per gli eventuali errori prodotti dal metodo produce()                              # Trigger any available delivery report callbacks from previous produce() calls
                                
        #invia un messaggio in mdoo asincrono 
        self.client_producer.produce(topic=topic_to_use, key=str(uuid4()), 
                                     value=str_to_send, on_delivery=self.delivery_report)
        
        self.client_producer.flush()
        
        # Asynchronously produce a message, the delivery report callback
        # will be triggered from poll() above when the message has been successfully delivered or failed permanently.
        
        
    def produce_file(self, topic_to_use, jsonfile_to_send):
        jsondict = json.load(open(jsonfile_to_send))
        jsonbytes = json.dumps(jsondict, indent=2).encode('utf-8')
        # Trigger any available delivery report callbacks from previous produce() calls
        self.client_producer.poll(0)

        # Asynchronously produce a message, the delivery report callback
        # will be triggered from poll() above when the message has been successfully delivered or failed permanently.
        self.client_producer.produce(topic=topic_to_use, key=str(uuid4()), value=jsonbytes, on_delivery=self.delivery_report)
        
        self.client_producer.flush()