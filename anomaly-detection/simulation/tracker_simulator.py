
from fileinput import filename
import time
from confluent_kafka import Producer
from uuid import uuid4
import json
from os import listdir
from os.path import isfile, join

class producer_simul_coords():
    def __init__(self, config):
        self.client_producer = Producer(config)
    
    def delivery_report(self, errmsg, msg):
        if errmsg is not None:
            print("[producer]: Delivery failed for Message: {} : {}".format(msg.key(), errmsg))
        
        #print('[producer]: Message: {} successfully produced to Topic: {} Partition: [{}] at offset {}'.format( DA DECOMMENTAREEEE EE E E EE EE EE E E E  EE 
       #     msg.value(), msg.topic(), msg.partition(), msg.offset()))
        
        
    def produce(self,topic_to_use, str_to_send):
        jsonbytes = json.dumps(str_to_send, indent=2).encode('utf-8')
        # Trigger any available delivery report callbacks from previous produce() calls
        self.client_producer.poll(0)

        # Asynchronously produce a message, the delivery report callback
        # will be triggered from poll() above when the message has been successfully delivered or failed permanently.
        self.client_producer.produce(topic=topic_to_use, key=str(uuid4()), value=jsonbytes, on_delivery=self.delivery_report)
        
        self.client_producer.flush()
        
        
    def produce_file(self, topic_to_use, jsonfile_to_send):
        jsondict = json.load(open(jsonfile_to_send))
        jsonbytes = json.dumps(jsondict, indent=2).encode('utf-8')
            # Trigger any available delivery report callbacks from previous produce() calls
        self.client_producer.poll(0)

        # Asynchronously produce a message, the delivery report callback
        # will be triggered from poll() above when the message has been successfully delivered or failed permanently.
        self.client_producer.produce(topic=topic_to_use, key=str(uuid4()), value=jsonbytes, on_delivery=self.delivery_report)
        
        self.client_producer.flush()
        
    def simulate_produce_streamingdata(self, topic_to_produce,  directory):
        files = [f for f in listdir(directory) if isfile(join(directory, f))]
        i = 0
        leng = len(files) 
        while i < leng:
        
            js = json.load(open(directory + "frame" + str(i) + "_skeletonsPoints3D.json"))
            time.sleep(0.2) # simulate delay <-------------------------------------------------------
                
            self.client_producer.poll(0)
            
            print("frame i: " + str(i))
            str_json =  json.dumps(js)
            jsonbytes = str_json.encode("utf-8") 
            self.client_producer.produce(topic=topic_to_produce, key=str(uuid4()), value=jsonbytes, 
                                                    on_delivery=self.delivery_report)
            self.client_producer.flush()
            i+=1        

    def simulate_produce_oneframe(self, topic_to_produce,  directory, frame):
            
            js = json.load(open(directory + frame))
            
            self.client_producer.poll(0)
            
            str_json =  json.dumps(js)
            jsonbytes = str_json.encode("utf-8") 
            self.client_producer.produce(topic=topic_to_produce, key=str(uuid4()), value=jsonbytes, 
                                                    on_delivery=self.delivery_report)
            self.client_producer.flush()

            print("produced file:" + frame)
                


def main():
    config_producer = {'bootstrap.servers': "192.168.160.195:29092"}
    prod = producer_simul_coords(config=config_producer)

    topic_to_produce = "topic1"
    dataset_simulation_path = "../dataset/simulation1/"
    
    #prod.simulate_produce_oneframe(topic_to_produce,dataset_simulation_path, "frame160_skeletonsPoints3D.json")  # A scopo di test, qui invio soltanto il frame 160.
    prod.simulate_produce_streamingdata(topic_to_produce,dataset_simulation_path) 

if __name__ == "__main__":
    main()
    