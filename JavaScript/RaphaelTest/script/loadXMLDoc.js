function loadXMLDoc(xmlName) {
    if (typeof XMLHttpRequest == 'undefined') {
        XMLHttpRequest = function () {
            try {
                return new ActiveXObject('Msxml2.XMLHTTP.6.0');
            } catch (e) {}
            try {
                return new ActiveXObject('Msxml2.XMLHTTP.3.0');
            } catch (e) {}
            try {
                return new ActiveXObject('Msxml2.XMLHTTP');
            } catch (e) {}
            return false;
        };
    }
    var request = new XMLHttpRequest();
    request.open("GET", xmlName, false);
    request.send();
    return request.responseXML;
}
