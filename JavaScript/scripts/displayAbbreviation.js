// 提取 title 属性并显示出来
function displayAbbreviation() {
    // 获取 abbr 元素
    var abbreviations = document.getElementsByTagName("abbr");
    // 判断文档里是否有缩略语
    if (abbreviations.length < 1) {
        return false;
    }
    // 定义一个数组存储数据
    var defs = [];
    for (var index = 0; index < abbreviations.length; index++) {
        var definition = abbreviations[index].getAttribute("title");
        var key = abbreviations[index].lastChild.nodeValue;
        defs[key] = definition;
    }


    var dlist = document.createElement("dl");
    // 遍历取值
    for (var sub_key in defs) {
        var sub_definition = defs[sub_key];
        var dtitle = document.createElement("dt");
        var dtitle_text = document.createTextNode(sub_key);
        dtitle.appendChild(dtitle_text);
        var ddesc = document.createElement("dd");
        var ddesc_text = document.createTextNode(sub_definition);
        ddesc.appendChild(ddesc_text);
        dlist.appendChild(dtitle);
        dlist.appendChild(ddesc);
    }
    // 创建标题
    var header = document.createElement("h2");
    var header_text = document.createTextNode("Abbreviation");
    header.appendChild(header_text);
    document.body.appendChild(header);
    document.body.appendChild(dlist);
    // 或者document.getElementByTagName("body")[0].appendChild(header);
}
window.onload = displayAbbreviation;
// addLoadEvent(displayAbbreviation); // 这个更方便把多个时间添加到 window.onload处理函数上
