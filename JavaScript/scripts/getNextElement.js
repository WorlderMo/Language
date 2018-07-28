// 获得元素的下一个元素节点，是 nextSibling的改进版本
// 通过传递元素的 nextSibling节点获取真正的下一个元素节点
function getNextElement(node) {
    if (node.nodeType == 1) {
        return node;
    }
    if (node.nextSibling) {
        return getNextElement(node.nextSibling);
    }
    return null;
}
