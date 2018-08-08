var paper = new Raphael(0, 0, 944, 847); // 可以通过<g>元素的第二个元素来确定其参数，使其更通用

function draw() {
    xmlDoc = loadXMLDoc("test-svg.xml");
    var gLists = xmlDoc.getElementsByTagName('g');
    for (const index in gLists) {
        const childElements = gLists[index].childNodes;
        for (const key in childElements) {
            var child = childElements[key];

            function $childAttr(attr) {
                return childElements[key].getAttribute(attr);
            }
            // 如果不是元素节点，则跳过
            if (child.nodeType !== 1) {
                continue;
            }
            // 如果是 rect
            if (child.nodeName === 'rect') {
                var rx = Number($childAttr('x'));
                var ry = Number($childAttr('y'));
                var width = $childAttr('width');
                var height = $childAttr('height');
                var rect_fill = $childAttr('fill');
                var rectangle = paper.rect(rx, ry, width, height);
                rectangle.attr('fill', rect_fill);
            }
            // 如果是 <use>
            if (child.nodeName === 'use') {
                var id = $childAttr('xlink:href');
                var sub_x = Number($childAttr('x'));
                var sub_y = Number($childAttr('y'));
                var sub_width = $childAttr('width');
                var sub_height = $childAttr('height');
                id = id.substr(1, id.length - 1);
                var symbol = xmlDoc.getElementById(id);
                var subChildren = symbol.childNodes;
                if ($childAttr('transform')) {
                    var sub_transform = String($childAttr('transform'));
                    sub_transform = "r" + sub_transform.substr(7, sub_transform.length - 8);
                }
                for (const subKey in subChildren) {

                    var subChild = subChildren[subKey];

                    function $subChildAttr(attr) {
                        return subChildren[subKey].getAttribute(attr);
                    }
                    // 如果不是元素节点，则跳过
                    if (subChild.nodeType !== 1) {
                        continue;
                    }
                    if (subChild.nodeName === 'text') {
                        var sub_tx = Number($subChildAttr('x'));
                        var sub_ty = Number($subChildAttr('y'));
                        var sub_fontFamily = $subChildAttr('font-family');
                        var sub_fontSize = $subChildAttr('font- size');
                        var sub_strokeWidth = $subChildAttr('stroke-width');
                        var sub_stroke = $subChildAttr('stroke');
                        var sub_text_fill = $subChildAttr('fill');
                        var sub_text_value = subChild.firstChild.nodeValue;
                        var sub_text = paper.text(sub_x + sub_tx, sub_y + sub_ty, sub_text_value);
                        sub_text.attr({
                            'font-family': sub_fontFamily,
                            'font-size': sub_fontSize,
                            'stroke-width': sub_strokeWidth,
                            'stroke': sub_stroke,
                            'fill': sub_text_fill
                        })
                    }

                    // 如果是<path>
                    if (subChild.nodeName === 'path') {
                        var sub_d = $subChildAttr('d');
                        if ($subChildAttr('stroke-width')) {
                            var sub_path_strokeWidth = $subChildAttr('stroke-width');
                        }
                        if ($subChildAttr('style')) {
                            var sub_style = $subChildAttr('style');
                            var sub_attrs=sub_style.split(";");
                            var sub_keyValue=[];
                            var sub_styleDict={};
                            for (var sub_attr in sub_attrs){
                                sub_keyValue=sub_attrs[sub_attr].split(":");
                                sub_styleDict[sub_keyValue[0]]=sub_keyValue[1];
                                sub_keyValue=[];
                            }
                        }

                        if ($subChildAttr('class')) {
                            var sub_class = $subChildAttr('class');
                        }
                        // if ($childAttr('transform')){
                        //     var sub_transform=$childAttr('transform');
                        //     sub_transform="r"+sub_transform.substr(7,sub_transform.length-2);
                        // }
                        // if ($subChildAttr('width')) {
                        //     var sub_width = $subChildAttr('width');
                        // }
                        // if ($subChildAttr('height')) {
                        //     var sub_height = $subChildAttr('height');
                        // }
                        if ($subChildAttr('stroke')) {
                            var sub_path_stroke = $subChildAttr('stroke');
                        }
                        var sub_path = paper.path(sub_d); // todo:绘制 path 的时候初始位置要加上<use>中的 x 和 y
                        sub_path.attr({
                            'stroke-width': sub_path_strokeWidth,
                            // 'style': sub_style, // todo :没有 style 属性，用；来分割获取元素
                            'class': sub_class,
                            'width': sub_width,
                            'height': sub_height,
                            'stroke': sub_path_stroke
                            // 'transform': sub_transform
                        });
                        sub_path.transform(sub_transform);
                        for (var i in sub_styleDict){
                            sub_path.attr(String(i),sub_styleDict[i]);
                        }
                    }

                    // 如果是<circle>
                    if (subChild.nodeName === 'circle') {
                        var sub_cx = Number($subChildAttr('cx'));
                        var sub_cy = Number($subChildAttr('cy'));
                        var sub_r = Number($subChildAttr('r'));
                        if ($subChildAttr('stroke')) {
                            var sub_circle_stroke = $subChildAttr('stroke');
                        }
                        if ($subChildAttr('stroke')) {
                            var sub_circle_strokeWidth = $subChildAttr('strokeWidth');
                        }
                        if ($subChildAttr('stroke')) {
                            var sub_circle_fill = $subChildAttr('fill');
                        }
                        if ($subChildAttr('class')) {
                            var sub_circle_class = $subChildAttr('class');
                        }
                        var sub_circle = paper.circle(sub_cx + sub_x, sub_cy + sub_y, sub_r);

                        sub_circle.attr({
                            'stroke': sub_circle_stroke,
                            'stroke-width': sub_circle_strokeWidth,
                            'fill': sub_circle_fill,
                            'class': sub_circle_class
                        })
                    }
                }
            }

            // 如果是<path>
            if (child.nodeName === 'path') {
                var d = $childAttr('d');
                if ($childAttr('stroke-width')) {
                    var path_strokeWidth = $childAttr('stroke-width');
                }
                if ($childAttr('class')) {
                    var path_class = $childAttr('class');
                }
                if ($childAttr('style')) {
                    var path_style = $childAttr('style');
                    var path_attrs=path_style.split(";");
                    var path_keyValue=[];
                    var path_styleDict={};
                    for (var path_attr in path_attrs){
                        path_keyValue=path_attrs[path_attr].split(":");
                        path_styleDict[path_keyValue[0]]=path_keyValue[1];
                        path_keyValue=[];
                    }
                }
                if ($childAttr('stroke')) {
                    var path_stroke = $childAttr('stroke');
                }
                var path = paper.path(d);
                path.attr({
                    'stroke-width': path_strokeWidth,
                    'class': path_class,
                    // 'style': path_style,
                    'stroke': path_stroke
                });
                for (var j in path_styleDict){
                    path.attr(String(j),path_styleDict[j]);
                }
            }


            if (child.nodeName === 'text') {
                var tx = Number($childAttr('x'));
                var ty = Number($childAttr('y'));
                if ($childAttr('font-family')) {
                    var fontFamily = $childAttr('font-family');
                }
                if ($childAttr('font-size')) {
                    var fontSize = $childAttr('font-size');
                }
                if ($childAttr('stroke-width')) {
                    var strokeWidth = $childAttr('stroke-width');
                }
                if ($childAttr('stroke')) {
                    var stroke = $childAttr('stroke');
                }
                if ($childAttr('fill')) {
                    var text_fill = $childAttr('fill');
                }
                if ($childAttr('style')) {
                    var text_style = $childAttr('style');
                    var text_attrs=text_style.split(";");
                    var text_keyValue=[];
                    var text_styleDict={};
                    for (var text_attr in text_attrs){
                        text_keyValue=text_attrs[text_attr].split(":");
                        text_styleDict[text_keyValue[0]]=text_keyValue[1];
                        text_keyValue=[];
                    }
                }
                var text_value = child.firstChild.nodeValue;
                var text = paper.text(tx, ty, text_value);
                text.attr({
                    'font-family': fontFamily,
                    'font-size': fontSize,
                    'stroke-width': strokeWidth,
                    'stroke': stroke,
                    'fill': text_fill,
                    // 'style': style
                });
                for (var k in text_styleDict){
                    text.attr(String(k),text_styleDict[k]);
                }
            }
            // todo:transform、图形
        }
    }

}
addLoadEvent(draw);
