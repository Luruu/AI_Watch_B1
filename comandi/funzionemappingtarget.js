
// QUESTO FILE SERVE PER MOSTRARE LA FUNZIONE IN MODO LEGGIBILE. 
function mapFromDittoProtocolMsg(namespace, id, group, channel, criterion, action, path, dittoHeaders, value, status, extra) {
    let jsonPayload = value.coordinates.properties;
    let textPayload = JSON.stringify(jsonPayload);
    let bytePayload = null;
    let contentType = 'text/plain; charset=UTF-8';
    return Ditto.buildExternalMsg(dittoHeaders, textPayload, bytePayload, contentType);
}