import csv
import json  

import matplotlib.pyplot as plt
import csv
  
eader = ['x','y']
jsondict = json.load(open("output.json"))

#questo tool è utile per creare file csv in modo da poterne successivamente creare dei grafici da visualizzare.
with open('file.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
            
    # write the header
   # writer.writerow(header)

    i = 1
    for c in jsondict["coordinates"]:
        writer.writerow([i, c["anomaly_score"]])
        i = i +1
            


x = []
y = []

x = []
y = []
  
with open('file.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(row[0])
        y.append(row[1])
  
plt.plot(x, y, color = 'g', linestyle = 'dashed',
         marker = 'o',label = "Weather Data")
  
plt.xticks(rotation = 25)
plt.xlabel('n coords')
plt.ylabel('anomaly score')
plt.title('Anomaly values', fontsize = 20)
plt.grid()
plt.legend()
plt.show()