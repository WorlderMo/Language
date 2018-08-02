function paintContainer() {
    var element=document.getElementById("container");
    var paper=new Raphael(element,500,500);
    var circle=paper.circle(100,100,80);
}
addLoadEvent(paintContainer);
