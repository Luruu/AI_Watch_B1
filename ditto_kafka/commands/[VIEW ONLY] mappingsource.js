
// QUESTO FILE SERVE PER MOSTRARE LA FUNZIONE IN MODO LEGGIBILE. 
function mapToDittoProtocolMsg(headers, textPayload, bytePayload, contentType) {
    const jsonString = String.fromCharCode.apply(null, new Uint8Array(bytePayload));
    const jsonData = JSON.parse(jsonString);
    const thingId = jsonData.thingId.split(':'); 
    const value = {
        coordinates: {
            properties: {
            }
        }
    };
    Object.assign(value['coordinates'][['properties']], jsonData);
    return Ditto.buildDittoProtocolMsg(thingId[0], thingId[1], 'things', 'twin', 'commands', 'modify', '/features', headers, value);
}

