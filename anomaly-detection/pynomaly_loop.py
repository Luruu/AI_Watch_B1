import json
import numpy as np
from random import randrange
import threading
from pysad.models import LocalOutlierProbability

# PyNomaly LooP -> Local Outlier Probability
class pynomaly_loop():
    
    def __init__(self,dataset):
        self.dataset_initialtraining_path = dataset 
        self.model  = None 
        if dataset != None: #Esegue l'addestarmento se è stato passato un dataset al costruttore, altriment viene effettuato successivamente.
            self.set_model_initial_training()
            


    def set_model_initial_training(self):
        json_dataset = json.load(open(self.dataset_initialtraining_path))
        coords_list = []
        for coord in json_dataset:
            coords_list.append([coord["x"], coord["y"], coord["z"] #, coord["x_rotation"], coord["y_rotation"], coord["z_rotation"], coord["w_rotation"]
                                ]) 
        n_coords = 3 #x, y, z per ora 
        matrix_xyz = np.reshape(coords_list,(-1,n_coords)) # where -1 infers the size of the new dimension from the size of the input array. n_coords sono il numero di righe.
        print("----------------------------------------------------------")
        print("[AnomalyDetector]: dataset for initial training: \n", matrix_xyz)
        print("----------------------------------------------------------")
        print(" [[WAIT]] --- [AnomalyDetector]: Initial training data to calibrate the model in progress (it takes seconds or minutes).... ")
        self.model = LocalOutlierProbability(matrix_xyz,2,1) 
       


    # this function returns True for anomaly, false otherwhise.
    def check_value_anomaly(self,anomaly_score):
        theshold = 0.45 # score >= theshold
        return 1 if anomaly_score >= theshold else 0 # 1 and 0 and not bool because after I have this problem: type bool is not json serializable.
        
        

    # test only! ---------    
    def simulate_anomaly_detection(self):
        return randrange(2) # Integer from [0 to 1] 



    #add anomaly value in the msg to produce.
    def setmsg_and_output_detection(self,queue_coords_anomaly, outputClass, anomaly_score, msg_dict, detection_val):
        msg_dict["People"][0]["skeleton"][8]["anomaly"] = detection_val
        
        queue_coords_anomaly.put(json.dumps(msg_dict))
        msg_dict["People"][0]["skeleton"][8]["anomaly_score"] = anomaly_score 
        outputClass.coordinates.append(msg_dict)

    
    
    def do_detection(self,queue_coords, queue_coords_anomaly, outputClass, path_initialtraining):
        if self.model == None:
            self.dataset_initialtraining_path = path_initialtraining
            self.set_model_initial_training()
        
        print("[[READY]] --- [AnomalyDetector]: ready to detect     "  + threading.current_thread().name)
        while True:
            msg_dict = json.loads(queue_coords.get())
            pointID8 = msg_dict["People"][0]["skeleton"][8]
            coordinates_array = np.array([pointID8["x"], pointID8["y"], pointID8["z"]
                     #   ,msg_dict["x_rotation"], msg_dict["y_rotation"], msg_dict["z_rotation"], msg_dict["w_rotation"]
                                       ])
       
            anomaly_score = self.model.fit_score_partial(coordinates_array)                                                    
      
            anomaly_value = self.check_value_anomaly(anomaly_score=anomaly_score) # True = anomaly        False = normal
            self.setmsg_and_output_detection(queue_coords_anomaly = queue_coords_anomaly, outputClass = outputClass, 
                                             anomaly_score = anomaly_score, msg_dict=msg_dict,detection_val=anomaly_value)
            
            print("[AnomalyDetector] Person 0, point 8!!: frame:", msg_dict["ID_Frame"], "x:" , pointID8["x"], "y:" , pointID8["y"], "z:" , pointID8["z"] 
                  # , "x_rotation:" , msg_dict["x_rotation"] , "y_rotation:" , msg_dict["y_rotation"], "w_rotation:" 
                  # , msg_dict["w_rotation"], "z_rotation:" , msg_dict["z_rotation"] msg_dict["z"]
              , "anomaly_score:" , anomaly_score,  "anomaly:" , anomaly_value)   
            
    
    