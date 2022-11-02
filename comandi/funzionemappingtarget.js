

/* --OLD DATI RENATO (ambiente virtuale)
function mapFromDittoProtocolMsg(namespace, id, group, channel, criterion, action, path, dittoHeaders, value, status, extra) {
    let textPayload = '{\"x\":' + value.coordinates.properties.x + ',\"y\":' + value.coordinates.properties.y + ',\"z\":' + 
    value.coordinates.properties.ID_Frame + ',\"x_rotation\":' + value.coordinates.properties.x_rotation + ',\"y_rotation\": ' + 
    value.coordinates.properties.y_rotation + ', \"z_rotation\": ' + value.coordinates.properties.z_rotation + ',\"w_rotation\":' + 
    value.coordinates.properties.w_rotation + ',\"idCamera\":\"' + 0 + '\"}';
    let bytePayload = null;
    let contentType = 'text/plain; charset=UTF-8';
    return Ditto.buildExternalMsg(dittoHeaders, textPayload, bytePayload, contentType);
} */

/*  1 COORD DDENNY (ambiente reale) PER LA FUNZIONE DI MAPPING
function mapFromDittoProtocolMsg(namespace, id, group, channel, criterion, action, path, dittoHeaders, value, status, extra) {
    let a = value.coordinates.properties;
    let textPayload = '{\"id_frame\":' + a.ID_Frame + 
    ',\"x\":' + a.People[0].skeleton[8].x + 
    ',\"y\":' + a.People[0].skeleton[8].y +
    ',\"z\":' + a.People[0].skeleton[8].z +
    ',\"x_rotation\":' + a.People[0].skeleton[8].x_rotation +
    ',\"y_rotation\":' + a.People[0].skeleton[8].y_rotation +
    ',\"z_rotation\":' + a.People[0].skeleton[8].z_rotation +
    ',\"w_rotation\":' + a.People[0].skeleton[8].w_rotation +
    ',\"confidence\":' + a.People[0].skeleton[8].confidence +
    ',\"pointID\":' + a.People[0].skeleton[8].pointID +
    '}';
    let bytePayload = null;
    let contentType = 'text/plain; charset=UTF-8';
    return Ditto.buildExternalMsg(dittoHeaders, textPayload, bytePayload, contentType);
}
*/

function mapFromDittoProtocolMsg(namespace, id, group, channel, criterion, action, path, dittoHeaders, value, status, extra) {
    let jsonPayload = value.coordinates.properties;
    let textPayload = JSON.stringify(jsonPayload);
    let bytePayload = null;
    let contentType = 'text/plain; charset=UTF-8';
    return Ditto.buildExternalMsg(dittoHeaders, textPayload, bytePayload, contentType);
}