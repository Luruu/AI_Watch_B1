# Comandi principali per docker

# DA MODIFICARE!!!!!!!!!!!!!!!!!!!!!!!!!!!!

https://github.com/eclipse/ditto/blob/master/deployment/docker/README.md 
docker-compose up -d   //crea e avvia i container
docker-compose logs -f //vedi logs
docker-compose down //cancella i container e stoppandoli

Altri comandi : https://docs.docker.com/compose/reference/


# COMANDI principali per configurare Ditto da utilizzare in ordine: 


curl -X PUT 'http://localhost:8080/api/2/policies/aiwatch:laboratorio-corridoio_dt' -u 'ditto:ditto' -H 'Content-Type: application/json' -d @policy.json

curl -X PUT 'http://localhost:8080/api/2/things/digitaltwin:Laboratorio_Corridoio' -u 'ditto:ditto' -H 'Content-Type: application/json' -d @digitaltwin.json

curl -X POST 'http://localhost:8080/devops/piggyback/connectivity?timeout=10' -u 'devops:foobar' -H 'Content-Type: application/json' -d @connectionSource.json

curl -X POST 'http://localhost:8080/devops/piggyback/connectivity?timeout=10' -u 'devops:foobar' -H 'Content-Type: application/json' -d @connectionTarget.json


# COMANDI principali per configurare kafka e per avviare un consumer
1) sudo docker-compose up (aggiungendo -d si può non bloccare il terminale ma parrebbe no far visualizzare l'output a docker ps successivamente) nella cartella docker (vedere nella documentazione come spegnere i container e avviarli senza cancellarli e crearli ogni volta)
    dovrebbe essere sudo docker-compose restart, solo che così facendo pare che non
2) Eseguire i comandi qui in alto in ordine nella cartella comandi
3) Avviare un consumer usando il container di kafka. 
  3.1) visualizza i container attivi e vedi l'id di kafka: sudo docker ps (IMPORTANTE USARE SUDO. ALTRIMENTI NON STAMPA NIENTE.)
  3.2) docker exec -it ID_KAFKA_DETTO_PRIMA sh
  3.3) usa il classico comando: 
kafka-console-consumer --bootstrap-server 192.168.160.195:29092 --topic topic_unity

