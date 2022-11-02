'''
Questo programma è il programma che si occupa di rigirare il messaggio dalle camere a unity 
e di dire a unity se una determinata coordinata (x,y,z,x_rotation, etc..) se è anomala o meno.
Al momento, finché non si hanno le telecamere, è utilizzato insieme ad un programma che simula l'invio delle coordinate in tempo reale (si trova in streaming-simulation/simulation_camere.py)
'''

import kafka
from pynomaly_loop import pynomaly_loop
#from message import message
from output import output

import threading
from queue import Queue

# ------------------------------------------------------------------------ SCRIVERE LE GUIDE !!!! -----------------------------------------------
#
#
#
#
#
#
def main():
    #semaphore_consumer_ad = threading.Semaphore(0) #sincronizzazione  tra consumer e anomaly detection
    #semaphore_ad_producer = threading.Semaphore(0) #sincronizzazione tra anomaly detection thread e producer
    
    n_partitions = 3
    replica = 1
    
    ip_broker = '192.168.160.195'
    port_broker = '9092'
    
    topics = ["topic_ditto","topic_unity","topic_ditto_reply","topic1","topic2","topic3","topic_test"]
    
    config_consumer = {
        'bootstrap.servers': ip_broker + ':' + port_broker,
        'group.id': 'anomaly_detector_group',
        'auto.offset.reset': 'latest' # o earliest o none (genera eccezione)
    }
    
    config_producer = {
        'bootstrap.servers': ip_broker + ':' + port_broker
    }
    
    path_initialtraining = "dataset/training_setOTTOBRE2022.json"
    
    admin = kafka.admin_client(ip_broker, port_broker)
    
    # admin.delete_topics(topics) # utile nel caso in cui si volesse rimuovere tutti i topic che sono stati creati per crearli da capo.
    
    admin.create_topics(topics, n_partitions, replica)
    
    topics_to_consume = [topics[0]]
    
    topic_to_produce = topics[1] 
   
    objconsumer = kafka.consumer_client(config_consumer, topics_to_consume)
    
    objproducer = kafka.producer_client(config_producer)
    
    queue_coords = Queue(maxsize = 100)
    queue_coords_anomaly = Queue(maxsize = 100) 
    
    output_class = output(path_initialtraining)
    
    task_consumer = threading.Thread(target=objconsumer.consume_forever, daemon=True, args=(queue_coords,))
    task_consumer.start()
    
    objanomaly_detection = pynomaly_loop(None)     #None = Non passo al costruttore il path_initialtraining (ma lo passo a do_detection) perché faccio l'addestramento in do_detection (quindi dal thread "task_anomaly_detection")
    task_anomaly_detection = threading.Thread(target=objanomaly_detection.do_detection, 
                daemon=True, args=(queue_coords, queue_coords_anomaly, output_class, path_initialtraining))    #daemon=true -> il thread si arresta quando si arresta quello principale (il main)
    task_anomaly_detection.start()
    
    task_producer = threading.Thread(target=objproducer.produce_forever, daemon=True, args=(
        topic_to_produce,queue_coords_anomaly)) 
    task_producer.start()

    
    input("[ PRESS ENTER TO EXIT AT ANY TIME (and save output) ] \n")
    output_class.save_output() #le coordinate sono aggiunte al dizionario da un metodo richiamato all'interno del metodo do_detection della classe anomaly_detection 
    print("[main]: closing..")
    

if __name__ == "__main__":
    main()
