function getHTTPObject() {
    // 对象检测
    if (window.XMLHttpRequest) {
        // 所有现代浏览器创建 XMLHttpRequest对象
        return new XMLHttpRequest();
    } else {
        // IE5,IE6浏览器创建 ActiveX对象
        return new ActiveXObject("Microsoft.XMLHTTP");
    }
}
