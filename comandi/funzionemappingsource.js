
/* ---------OLD (dati ottenuti dall'ambiente virtuale)
function mapToDittoProtocolMsg(headers, textPayload, bytePayload, contentType) {
    const jsonString = String.fromCharCode.apply(null, new Uint8Array(bytePayload));
    const jsonData = JSON.parse(jsonString);
    const thingId = jsonData.thingId.split(':');
    const value = {
        coordinates: {
            properties: {
                x: jsonData.x,
                y: jsonData.y,
                z: jsonData.z,
                x_rotation: jsonData.x_rotation,
                y_rotation: jsonData.y_rotation,
                z_rotation: jsonData.z_rotation,
                w_rotation: jsonData.w_rotation
            }
        }
    };
    return Ditto.buildDittoProtocolMsg(thingId[0], thingId[1], 'things', 'twin', 'commands', 'modify', '/features', headers, value);
}
*/

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

