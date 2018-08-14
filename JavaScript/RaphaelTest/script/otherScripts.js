function splitStyle(style) {
    var attrs=style.split(';');
    var keyValueList;
    var styleDict={};
    for (var i in attrs) {
        keyValueList=attrs[i].split(':');
        styleDict[keyValueList[0]]=keyValueList[1];
        keyValueList=[];
    }
    return styleDict;
}
