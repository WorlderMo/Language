/*
 * @Author: mohailang (1198534595@qq.com)
 * @Date: 2018-08-12 22:07:51
 * @Last Modified by: mohailang
 * @Last Modified time: 2018-08-16 08:57:32
 */
var windowWidth = Math.max(
    document.documentElement.clientWidth,
    window.innerWidth
);

var windowHeight = Math.max(
    document.documentElement.clientHeight,
    window.innerHeight
);

// var paper = new Raphael(0, 0, 944, 847);

function dynamicDraw() {
    xmlDoc = loadXMLDoc("test-svg.svg");
    var AllSymbolElements = xmlDoc.getElementsByTagName('symbol');
    var gLists = xmlDoc.getElementsByTagName('g');
    for (var index = 0; index < gLists.length; index++) {
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
                var paper = new Raphael(rx, ry, width, height);
                var rectangle = paper.rect(rx, ry, width, height);
                rectangle.attr({
                    'fill': rect_fill
                });
            }

            // 如果是<use>节点，里面引用了<symbol>，含有多个元素
            if (gKid.nodeName === 'use') {
                var id = getAttr('xlink:href');
                id = id.substring(1);
                var use_x = Number(getAttr('x'));
                var use_y = Number(getAttr('y'));
                var use_width = Number(getAttr('width'));
                var use_height = Number(getAttr('height'));

                // 获取 symbol元素
                // var symbol = xmlDoc.getElementById(id);

                for (var j = 0; j < AllSymbolElements.length; j++) {
                    if (AllSymbolElements[j].getAttribute('id') === id) {
                        symbol=AllSymbolElements[j];
                        break;
                    }
                }

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

                    var use_transform_parsed = 't' + use_x + ',' + use_y + 'r' + transform_r + ',' + offset_x + ',' + offset_y + 's' + scale + ',' + scale + ',0,0';

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

                        var symbol_path = paper.path(symbol_path_d);

                        symbol_path.attr({
                            'stroke-width': symbol_path_strokeWidth,
                            'class': symbol_path_class,
                            'stroke': symbol_path_stroke
                        });
                        if (getSubAttr('style')) {
                            var symbol_path_style = getSubAttr('style');
                            var symbol_path_style_parsed = parsed_style(symbol_path_style);
                            symbol_path.attr(symbol_path_style_parsed);
                        }
                        // transform
                        symbol_path.attr({
                            transform: use_transform_parsed
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
                            transform: use_transform_parsed
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

                if (getAttr('stroke')) {
                    var path_stroke = getAttr('stroke');
                }

                var path = paper.path(path_d);

                path.attr({
                    'stroke-width': path_strokeWidth,
                    'class': path_class,
                    'stroke': path_stroke
                });
                if (getAttr('style')) {
                    var path_style = getAttr('style');
                    var path_style_parsed = parsed_style(path_style);
                    path.attr(path_style_parsed);
                }

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
                if (getAttr('style')) {
                    var text_style = getAttr('style');
                    var text_style_parsed = parsed_style(text_style);
                    text.attr(text_style_parsed);
                }
                text.attr({
                    'font-family': text_fontFamily,
                    'font-size': text_fontSize,
                    'stroke-width': text_strokeWidth,
                    'stroke': text_stroke,
                    'fill': text_fill
                });


            }
        }
    }
}

addLoadEvent(dynamicDraw);
