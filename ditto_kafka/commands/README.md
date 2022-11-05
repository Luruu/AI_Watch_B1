# SETUP ECLIPSE DITTO FOR AIWATCH PROJECT

# DA MODIFICARE!!!!!!!!!!!!!!!!!!!!!!!!!!!!

https://github.com/eclipse/ditto/blob/master/deployment/docker/README.md 
docker-compose up -d   //crea e avvia i container
docker-compose logs -f //vedi logs
docker-compose down //cancella i container e stoppandoli

Altri comandi : https://docs.docker.com/compose/reference/


# COMANDI principali per configurare Ditto da utilizzare in ordine: 


curl -X PUT 'http://localhost:8080/api/2/policies/aiwatch:policy' -u 'ditto:ditto' -H 'Content-Type: application/json' -d @policy.json

curl -X PUT 'http://localhost:8080/api/2/things/digitaltwin:Laboratorio_Corridoio' -u 'ditto:ditto' -H 'Content-Type: application/json' -d @digitaltwin.json

curl -X POST 'http://localhost:8080/devops/piggyback/connectivity?timeout=10' -u 'devops:foobar' -H 'Content-Type: application/json' -d @create_connectionSource.json

curl -X POST 'http://localhost:8080/devops/piggyback/connectivity?timeout=10' -u 'devops:foobar' -H 'Content-Type: application/json' -d @create_connectionTarget.json
