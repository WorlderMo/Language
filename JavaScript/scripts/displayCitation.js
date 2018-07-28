// 显示“文献来源链接表”
function displayCitation() {
    // 取得所有引用
    var quote = document.getElementsByTagName("blockquote");
    // 变量引用
    for (var i = 0; i < quote.length; i++) {
        // 如果没有 cite 属性，继续下一次循环
        if (!quote[i].getAttribute("cite")) {
            continue;
        }
        // 保存 cite属性
        var url = quote[i].getAttribute("cite");
        // 取得引用中的所有元素节点
        var quoteChildren = quote[i].getElementsByTagName("*");
        // 如果没有元素节点，就继续下一次循环
        if (quoteChildren.length < 1) {
            continue;
        }
        // 取得引用中的最后一个元素节点
        var lastElement = quoteChildren[quoteChildren.length - 1];
        // 创建标记
        var link = document.createElement("a");
        var link_text = document.createTextNode("source");
        link.appendChild(link_text);
        link.setAttribute("href", url);
        var superscript = document.createElement("sup");
        superscript.appendChild(link);
        // 把标记添加到引用中的最后一个元素节点
        lastElement.appendChild(superscript);
    }
}
addLoadEvent(displayCitation);
