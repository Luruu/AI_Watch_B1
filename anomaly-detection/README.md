# SETUP STREAMING ANOMALY DETECTOR

# DA MODIFICARE COMPLETAMENTE!!!!! 02-11-2022!

# DTProject


# Macchina utilizzata
iMac (Retina 5K, 27-inch, 2020)
macOS Monterey 12.0.1 (21A559)
Processore 3,6 GHz Intel Core i9 10 core (nota: è possibile (ma non è certo) che ci siano problemi con m1)
Memoria 32 GB 2667 MHz DDR4

# SETUP 
Questo modulo del progetto AIWATCH prevede i seguenti software: Docker, eclipse ditto, pysad, Apache kafka.

Riguardo Eclipse Ditto, è possibile installarlo in vari modi. Io ho scelto di usare ditto con docker (un'alternativa è kubernetes)
Il tutorial è stato pensato per essere eseguito linearmente.

# SETUP Apache kafka
La versione di kafka che ho utilizzato io è la versione 2.13-2.8.1. 
La guida basilare per usare kafka è qui: https://kafka.apache.org/intro , ma qui ti spiegherò come fare per impostare e avviare kafka nel contesto del progetto:

Setup:
Semplicemente basta impostare l'indirizzo ip della propria macchina nei file di configurazione di kafka che troverai al percorso "kafka_2.13-2.8.1/config":
Ovunque vedi "localhost" o un indirizzo ip, sostituiscilo con quello della tua macchina (al momento c'è un indirizzo IP privato perché lavoriamo in lan).

Avviare kafka:
Apri 5 terminali e in ognuno di questi vai in kafka_2.13-2.8.1 ed esegui i seguenti comandi in ordine:
Terminale 1 (avvia zookeper service): bin/zookeeper-server-start.sh config/zookeeper.properties
Terminale 2 (avvia il broker): bin/kafka-server-start.sh config/server.properties
I successivi 3 terminali servono per consumare sui 3 topic utilizzati in questo progetto (attualmente): "t1" (in cui scrivono le camere), "topic_ditto" (in cui scrive ditto) e "topic_unity" in cui scrive il programma "dtproject.py", cioè il programma che implementa l'anomaly detection.
Nota: il motivo per cui è utile consumare su questi 3 topic è per vedere se i dati vengono effettivamente scritti, quindi a scopo di test (ad esempio, magari le camere non riescono a scrivere nel topic t1 e quindi risulta utile avere un riscontro)
Terminale 3: Consuma su t1: bin/kafka-console-consumer.sh --topic t1 --bootstrap-server <INSERISCI_TUO_IP>:9092
Terminale 4: Consuma su topic_ditto: bin/kafka-console-consumer.sh --topic topic_ditto --bootstrap-server <INSERISCI_TUO_IP>:9092
Terminale 5: Consuma su topic_unity: bin/kafka-console-consumer.sh --topic topic_unity --bootstrap-server <INSERISCI_TUO_IP>:9092


# SETUP Docker
Scarica e installa Docker da questo link (selezionandola versione corretta in base al processore, se si è su mac o per il sistema operativo): https://www.docker.com/products/docker-desktop/

# SETUP Eclipse Ditto
Una volta installato Docker, è possibile avviare ditto.
Estrai il file ditto-master.zip in una cartella ed entraci (da terminale)

Dopodiché esegui i seguenti comandi per avviare i servizi:
```bash 
cd deployment/docker/
```
```bash 
sudo docker-compose up -d
```
Per vedere i logs:
```bash
sudo docker-compose logs -f
```
Ulteriori informazioni in merito sono reperibili qui: https://github.com/eclipse/ditto/blob/master/deployment/docker/README.md

Fatto questo, il webserver (nginx) dovrebbe essere attivo (insieme ad altri servizi di docker) e dovresti poter visualizzare questa pagina in locale: http://localhost:8080/.

Adesso è necessario creare le policy, i digital twins e le connessioni "source" e "target":
# [DA CONTINUARE E VEDERE DOVE e COME SCRIVERE QUESTA ROBA.] da aggiungere anche immagini. 


