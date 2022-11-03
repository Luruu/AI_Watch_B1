
// QUESTO FILE SERVE PER MOSTRARE LA FUNZIONE IN MODO LEGGIBILE. 
function mapToDittoProtocolMsg(headers, textPayload, bytePayload, contentType) {
    const jsonString = String.fromCharCode.apply(null, new Uint8Array(bytePayload));
    const jsonData = JSON.parse(jsonString);
    const thingId = jsonData.thingId.split(':'); //da controllare se il json è vuoto o non ha i campi che ci si aspetta (altrimenti appaiono errori nel topic topic_ditto_reply ovviamente)
    const value = {
        coordinates: {
            properties: {
            }
        }
    };
    Object.assign(value['coordinates'][['properties']], jsonData);
    return Ditto.buildDittoProtocolMsg(thingId[0], thingId[1], 'things', 'twin', 'commands', 'modify', '/features', headers, value);
}

