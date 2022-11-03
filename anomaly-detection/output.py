'''         OUTPUT CLASS
Questa classe ha l'obiettivo di salvare in maniera persisente l'output del modulo di streaming anomaly detection.
'''

import json

class output():
    def __init__(self, path1):
        self.path_initiltraining = path1
        self.coordinates = []
        
        
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=False, indent=4)
    
    
    def save_output(self):
        with open('output.json', 'w', encoding='utf-8') as f:
            f.write(self.to_json())