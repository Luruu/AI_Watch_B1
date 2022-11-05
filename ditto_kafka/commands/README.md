# SETUP ECLIPSE DITTO FOR AIWATCH PROJECT

## Utilities
You can find:
- **[highly recommended]** Eclipse Ditto **v 2.4** documentation [here](https://www.eclipse.org/ditto/2.4/intro-overview.html) to understand the operations carried out below but also to understand how to do other operations.
- Eclipse Ditto repository [here](https://github.com/eclipse-ditto/ditto).
- Examples of using Eclipse Ditto [here](https://github.com/eclipse-ditto/ditto-examples).

## BASIC OPERATIONS TO DO

1. Open a new terminal and go in ```AI_WATCH_B1/ditto_kafka/commands```
2. Create a new policy
```bash
curl -X PUT 'http://localhost:8080/api/2/policies/aiwatch:policy' -u 'ditto:ditto' -H 'Content-Type: application/json' -d @policy.json
```
3. Create a new digital twin
```bash
curl -X PUT 'http://localhost:8080/api/2/things/digitaltwin:Laboratorio_Corridoio' -u 'ditto:ditto' -H 'Content-Type: application/json' -d @digitaltwin.json
```
4. Create a new kafka connection source from user "nginx:ditto" (A1 Module - Tracker)
```bash
curl -X POST 'http://localhost:8080/devops/piggyback/connectivity?timeout=10' -u 'devops:foobar' -H 'Content-Type: application/json' -d @create_connectionSource.json
```
5. Create a new kafka connection target from user "ditto:observer" (Software streaming anomaly detector)
```bash
curl -X POST 'http://localhost:8080/devops/piggyback/connectivity?timeout=10' -u 'devops:foobar' -H 'Content-Type: application/json' -d @create_connectionTarget.json
```
***

## Javascript Mapping Functions used
Below is shown on several lines the mapping function "mapToDittoProtocolMsg()" in javascript of the file ```connectionSource.json```
https://github.com/Luruu/AI_Watch_B1/blob/8be8fbda6f4e43c60fd3ccbc366bdff03f1869d0/ditto_kafka/commands/%5BVIEW%20ONLY%5D%20mappingsource.js#L3-L15

Below is shown on several lines the mapping function "mapFromDittoProtocolMsg()" in javascript of the file ```connectionTarget.json```
https://github.com/Luruu/AI_Watch_B1/blob/8be8fbda6f4e43c60fd3ccbc366bdff03f1869d0/ditto_kafka/commands/%5BVIEW%20ONLY%5D%20mappingtarget.js#L3-L9
