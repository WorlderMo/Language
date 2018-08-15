var windowWidth = Math.max(
    document.documentElement.clientWidth,
    window.innerWidth
);

var windowHeight = Math.max(
    document.documentElement.clientHeight,
    window.innerHeight
);

var paper = Raphael(0, 0, 9666, 9666); // 可以通过<g>元素的第二个元素来确定其参数，使其更通用

window.onload = function () {

    //禁止页面滚动
    //document.documentElement.style.overflow='hidden';

    var oImg = document.getElementById("my-canvas");
    var width = paper.width;
    var height = paper.height;
    var x = oImg.offsetLeft;
    var y = oImg.offsetTop;

    function fnWheel(obj, fncc) {
        obj.onmousewheel = fn;
        if (obj.addEventListener) {
            obj.addEventListener('DOMMouseScroll', fn, false);
        }

        function fn(ev) {
            var oEvent = ev || window.event;
            //down确定放大还是缩小
            var down = true;

            if (oEvent.detail) {
                down = oEvent.detail > 0
            } else {
                down = oEvent.wheelDelta < 0
            }

            if (fncc) {
                fncc.call(this, down, oEvent);
            }

            if (oEvent.preventDefault) {
                oEvent.preventDefault();
            }

            return false;
        }
    }
    fnWheel(oImg, function (down, oEvent) {
        //offsetWidth=width+2*boder
        var oldWidth = this.offsetWidth;
        var oldHeight = this.offsetHeight;
        var oldLeft = this.offsetLeft;
        var oldTop = this.offsetTop;
        //比例
        //clientX,clientY鼠标坐标
        var scaleX = (oEvent.clientX - oldLeft) / oldWidth;
        var scaleY = (oEvent.clientY - oldTop) / oldHeight;
        //scaleX,scaleY为鼠标与div左上角位置差与div长宽的比值
        var ncx = (oEvent.clientY - x) / width;
        var ncy = (oEvent.clientY - y) / height;
        var oldW = width;
        var oldH = height;

        if (down) {
            this.style.width = this.offsetWidth * 0.9 + "px";
            this.style.height = this.offsetHeight * 0.9 + "px";
            width = width / 0.9;
            height = height / 0.9;
        } else {
            this.style.width = this.offsetWidth * 1.1 + "px";
            this.style.height = this.offsetHeight * 1.1 + "px";

            width = width / 1.1;
            height = height / 1.1;
        }


        var newWidth = this.offsetWidth;
        var newHeight = this.offsetHeight;
        this.style.left = oldLeft - scaleX * (newWidth - oldWidth) + "px";
        this.style.top = oldTop - scaleY * (newHeight - oldHeight) + "px";
        paper.setViewBox(0, 0, width, height, false);


    });
}
//拖拽
var ie = document.all;
var nn6 = document.getElementById && !document.all;
var isdrag = false;
var y, x;
var oDragObj;

function moveMouse(e) {
    if (isdrag) {
        oDragObj.style.top = (nn6 ? nTY + e.clientY - y : nTY + event.clientY - y) + "px";
        oDragObj.style.left = (nn6 ? nTX + e.clientX - x : nTX + event.clientX - x) + "px";
        return false;
    }
}

function initDrag(e) {
    var oDragHandle = nn6 ? e.target : event.srcElement;
    var topElement = "HTML";
    while (oDragHandle.tagName != topElement && oDragHandle.className != "dragAble") {
        oDragHandle = nn6 ? oDragHandle.parentNode : oDragHandle.parentElement;
    }
    if (oDragHandle.className == "dragAble") {
        isdrag = true;
        oDragObj = oDragHandle;
        nTY = parseInt(oDragObj.style.top + 0);
        y = nn6 ? e.clientY : event.clientY;
        nTX = parseInt(oDragObj.style.left + 0);
        x = nn6 ? e.clientX : event.clientX;
        document.onmousemove = moveMouse;
        return false;
    }
}
document.onmousedown = initDrag;
document.onmouseup = new Function("isdrag=false");

function dynamicDraw() {
    xmlDoc = loadXMLDoc("test-svg.svg");
    var gLists = xmlDoc.getElementsByTagName('g');
    for (var index in gLists) {
        var childElements = gLists[index].childNodes;
        for (var key in childElements) {
            var gKid = childElements[key];
            // 如果不是元素节点，则跳过
            if (gKid.nodeType !== 1) {
                continue;
            }

            // 获取属性的函数
            function getAttr(attr) {
                return gKid.getAttribute(attr);
            }

            // 如果子节点是 rect
            if (gKid.nodeName === 'rect') {
                var rx = Number(getAttr('x'));
                var ry = Number(getAttr('y'));
                var width = getAttr('width');
                var height = getAttr('height');
                var rect_fill = getAttr('fill');
                var rectangle = paper.rect(rx, ry, width, height);
                rectangle.attr({
                    'fill': rect_fill
                });
            }

            // 如果是<use>节点，里面引用了<symbol>，含有多个元素
            if (gKid.nodeName === 'use') {
                var id = getAttr('xlink:href');
                id = id.substring(1);

                //获取use标签坐标长宽
                var use_x = Number(getAttr('x'));
                var use_y = Number(getAttr('y'));
                var use_width = Number(getAttr('width'));
                var use_height = Number(getAttr('height'));

                // 获取 symbol元素
                var symbol = xmlDoc.getElementById(id);

                // 获取 viewBox属性
                var symbol_viewBox = symbol.getAttribute('viewBox').split(' ');
                // 比例
                var scale = (use_height / Number(symbol_viewBox[3])).toFixed(2);
                var symbolChildren = symbol.childNodes;
                // 获取 <use>里transform的值
                if (getAttr('transform')) {
                    var use_transform = String(getAttr('transform'));
                    use_transform = use_transform.substring(7, use_transform.length - 1).split(',');
                    var transform_r = use_transform[0];
                    var transform_x = use_transform[1];
                    var transform_y = use_transform[2];

                    // 求得相对偏移量
                    var offset_x = (transform_x - use_x).toFixed(6);
                    var offset_y = (transform_y - use_y).toFixed(6);
                    // transform
                    var transforms = 't' + use_x + ',' + use_y + 'r' + transform_r + ',' + offset_x + ',' + offset_y + 's' + scale + ',' + scale + ',0,0';
                }
                for (var subKey in symbolChildren) {
                    var symbolKid = symbolChildren[subKey];

                    // 获取属性的函数
                    function getSubAttr(attr) {
                        return symbolKid.getAttribute(attr);
                    }

                    if (symbolKid.nodeType !== 1) {
                        continue;
                    }

                    if (symbolKid.nodeName === 'text') {
                        // 获取 text 各个属性
                        var symbol_text_x = Number(getSubAttr('x'));
                        var symbol_text_y = Number(getSubAttr('y'));
                        var symbol_text_fontFamily = getSubAttr('font-family');
                        var symbol_text_strokeWidth = getSubAttr('stroke-width');
                        var symbol_text_stroke = getSubAttr('stroke');
                        var symbol_text_fill = getSubAttr('fill');
                        var symbol_text_value = symbolKid.firstChild.nodeValue;

                        var symbol_text = paper.text(use_x + symbol_text_x, use_y + symbol_text_y, symbol_text_value);
                        symbol_text.attr({
                            'font-family': symbol_text_fontFamily,
                            'stroke-width': symbol_text_strokeWidth,
                            'stroke': symbol_text_stroke,
                            'fill': symbol_text_fill
                        });
                    }

                    if (symbolKid.nodeName === 'path') {
                        // 获取 path 的属性
                        var symbol_path_d = getSubAttr('d');
                        if (getSubAttr('stroke-width')) {
                            var symbol_path_strokeWidth = getSubAttr('stroke-width');
                        }

                        if (getSubAttr('class')) {
                            var symbol_path_class = getSubAttr('class');
                        }
                        if (getSubAttr('stroke')) {
                            var symbol_path_stroke = getSubAttr('stroke');
                        }
                        if (getSubAttr('style')) {
                            var symbol_path_style = getSubAttr('style');
                            var json = getJson(symbol_path_style);
                        }

                        var symbol_path = paper.path(symbol_path_d);
                        symbol_path.attr({
                            'stroke-width': symbol_path_strokeWidth,
                            'class': symbol_path_class,
                            'stroke': symbol_path_stroke
                            // fill:"#ff0000",stroke:"#ff0000","stroke-width":1
                        });

                        symbol_path.attr(json);
                        symbol_path.attr({
                            transform: transforms
                        });
                    }

                    if (symbolKid.nodeName === 'circle') {
                        var symbol_circle_x = Number(getSubAttr('cx'));
                        var symbol_circle_y = Number(getSubAttr('cy'));
                        var symbol_circle_r = Number(getSubAttr('r'));

                        if (getSubAttr('stroke')) {
                            var symbol_circle_stroke = getSubAttr('stroke');
                        }
                        if (getSubAttr('stroke-width')) {
                            var symbol_circle_stroke_width = getSubAttr('stroke-width');
                        }
                        if (getSubAttr('fill')) {
                            var symbol_circle_fill = getSubAttr('fill');
                        }
                        if (getSubAttr('class')) {
                            var symbol_circle_class = getSubAttr('class');
                        }

                        var symbol_circle = paper.circle(symbol_circle_x, symbol_circle_y, symbol_circle_r);
                        symbol_circle.attr({
                            'stroke': symbol_circle_stroke,
                            'stroke-width': symbol_circle_stroke_width,
                            'fill': symbol_circle_fill,
                            'class': symbol_circle_class
                        });

                        symbol_circle.attr({
                            transform: transforms
                        });
                    }
                }
            }

            if (gKid.nodeName === 'path') {
                var path_d = getAttr('d');
                if (getAttr('stroke-width')) {
                    var path_strokeWidth = getAttr('stroke-width');
                }
                if (getAttr('class')) {
                    var path_class = getAttr('class');
                }
                if (getAttr('style')) {
                    var path_style = getJson(getAttr('style'));
                }
                if (getAttr('stroke')) {
                    var path_stroke = getAttr('stroke');
                }

                var path = paper.path(path_d);
                path.attr({
                    'stroke-width': path_strokeWidth,
                    'class': path_class,
                    'stroke': path_stroke
                });
                path.attr(path_style);
            }

            if (gKid.nodeName === 'text') {
                var text_x = Number(getAttr('x'));
                var text_y = Number(getAttr('y'));
                if (getAttr('font-family')) {
                    var text_fontFamily = getAttr('font-family');
                }
                if (getAttr('font-size')) {
                    var text_fontSize = getAttr('font-size');
                }
                if (getAttr('stroke-width')) {
                    var text_strokeWidth = getAttr('stroke-width');
                }
                if (getAttr('stroke')) {
                    var text_stroke = getAttr('stroke');
                }
                if (getAttr('fill')) {
                    var text_fill = getAttr('fill');
                }

                var text_value = gKid.firstChild.nodeValue;
                var text = paper.text(text_x, text_y, text_value);
                text.attr({
                    'font-family': text_fontFamily,
                    'font-size': text_fontSize,
                    'stroke-width': text_strokeWidth,
                    'stroke': text_stroke,
                    'fill': text_fill
                });
                if (getAttr('style')) {
                    var text_style = getJson(getAttr('style'));
                }
                text.attr(text_style);

            }
        }
    }
}

addLoadEvent(dynamicDraw);
