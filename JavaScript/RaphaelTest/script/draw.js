var paper = new Raphael(0,0, 944, 847); // 可以通过<g>元素的第二个元素来确定其参数，使其更通用

function draw() {
    xmlDoc = loadXMLDoc("test-svg.xml");
    var gLists = xmlDoc.getElementsByTagName('g');
    for(const index in gLists){
        const childElements=gLists[index].childNodes;
        for(const key in childElements){
            // 如果不是元素节点，则跳过
            if (childElements[key].nodeType!==1){
                continue;
            }
            // 如果是 rect
            if (childElements[key].nodeName ==='rect'){
                var rx = childElements[key].getAttribute('x');
                var ry = childElements[key].getAttribute('y');
                var width=childElements[key].getAttribute('width');
                var height=childElements[key].getAttribute('height');
                var rect_fill=childElements[key].getAttribute('fill');
                var rectangle=paper.rect(rx,ry,width,height);
                rectangle.attr('fill',rect_fill);
            }
            // 如果是 <use>
            if (childElements[key].nodeName === 'use'){
                var id=childElements[key].getAttribute('xlink:href');
                var sub_tx=childElements[key].getAttribute('x');
                var sub_ty=childElements[key].getAttribute('y');
                id=id.substr(1,id.length-1);
                var symbol=xmlDoc.getElementById(id);
                var subChildren=symbol.childNodes;
                for (subkey in subChildren){
                    // 如果不是元素节点，则跳过
                    if (subChildren[subkey].nodeType!==1){
                        continue;
                    }
                    if (subChildren[subkey].nodeName === 'text'){
                        // var tx = subChildren[subkey].getAttribute('x');
                        // var ty = subChildren[subkey].getAttribute('y');
                        var sub_fontFamily = subChildren[subkey].getAttribute('fontFamily');
                        var sub_fontSize = subChildren[subkey].getAttribute('fontSize');
                        var sub_strokeWidth = subChildren[subkey].getAttribute('strokeWidth');
                        var sub_stroke = subChildren[subkey].getAttribute('stroke');
                        var sub_text_fill = subChildren[subkey].getAttribute('fill');
                        var sub_text_value = subChildren[subkey].firstChild.nodeValue;
                        var sub_text=paper.text(sub_tx,sub_ty,sub_text_value);
                        sub_text.attr({
                            'font-family':sub_fontFamily,
                            'font-size':sub_fontSize,
                            'stroke-width':sub_strokeWidth,
                            'stroke':sub_stroke,
                            'fill':sub_text_fill
                        })
                    }

                    // 如果是<path>
                    if (subChildren[subkey].nodeName === 'path'){
                        var sub_d=subChildren[subkey].getAttribute('d');
                        var sub_path_strokeWidth=subChildren[subkey].getAttribute('strokeWidth');
                        var sub_style=subChildren[subkey].getAttribute('style');
                        var sub_class=subChildren[subkey].getAttribute('class');
                        // var sub_transform=subChildren[key].getAttribute('transform');
                        var sub_path=paper.path(sub_d);
                        sub_path.attr({
                            'stroke-width':sub_path_strokeWidth,
                            'style':sub_style,
                            'class':sub_class
                            // 'transform':sub_transform
                        });
                    }
                }
            }

            // 如果是<path>
            if (childElements[key].nodeName === 'path'){
                var d=childElements[key].getAttribute('d');
                var path_strokeWidth=childElements[key].getAttribute('strokeWidth');
                var path_class=childElements[key].getAttribute('class');
                var path=paper.path(d);
                path.attr({
                    'stroke-width':path_strokeWidth,
                    'class':path_class
                });
            }


            if (childElements[key].nodeName === 'text'){
                var tx=childElements[key].getAttribute('x');
                var ty=childElements[key].getAttribute('y');
                var fontFamily = childElements[key].getAttribute('fontFamily');
                var fontSize = childElements[key].getAttribute('fontSize');
                var strokeWidth = childElements[key].getAttribute('strokeWidth');
                var stroke = childElements[key].getAttribute('stroke');
                var text_fill = childElements[key].getAttribute('fill');
                var style=childElements[key].getAttribute('style');
                var text_value = childElements[key].firstChild.nodeValue;
                var text=paper.text(tx,ty,text_value);
                text.attr({
                    'font-family':fontFamily,
                    'font-size':fontSize,
                    'stroke-width':strokeWidth,
                    'stroke':stroke,
                    'fill':text_fill,
                    'style':style
                });
            }
            // todo:transform、图形
        }
    }

}
addLoadEvent(draw);
