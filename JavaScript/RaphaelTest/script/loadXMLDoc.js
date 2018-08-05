function loadXMLDoc(xmlName) {
    if (window.XMLHttpRequest) {
        request = new XMLHttpRequest();
    } else {
        request = new ActiveXObject("Microsoft.XMLHTTP");
    }
    request.open("GET", xmlName, false);
    request.send(null);
    return request.responseXML;
}
