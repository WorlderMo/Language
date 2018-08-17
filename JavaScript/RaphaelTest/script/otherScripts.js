function parsed_style(style) {
    var oldStyle = style;
    var style_parse = '{';
    var sub_style = oldStyle.split(';');
    for (var i = 0; i < sub_style.length - 1; i++) {
        var sub = sub_style[i].split(':');
        style_parse = style_parse + '"' + sub[0] + '":' + '"' + sub[1] + '",'
    }
    sub = sub_style[sub_style.length - 1].split(':');
    style_parse = style_parse + '"' + sub[0] + '":"' + sub[1] + '"}';
    return JSON.parse(style_parse);
}
