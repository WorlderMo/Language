var oImg = document.getElementById("my-canvas");
var zoom = 1;

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
addLoadEvent(fnWheel);


var oldWidth = oImg.offsetWidth;
var oldHeight = oImg.offsetHeight;

fnWheel(oImg, function (down, oEvent) {
    var oldLeft = this.offsetLeft;
    var oldTop = this.offsetTop;
    //比例
    //clientX,clientY鼠标坐标
    var scaleX = (oEvent.clientX - oldLeft) / oldWidth;
    var scaleY = (oEvent.clientY - oldTop) / oldHeight;


    if (down) {
        if (zoom > 0.5) {
            zoom *= 0.81;
            this.style.zoom = zoom;
            var newWidth = oldWidth * 0.9;
            var newHeight = oldHeight * 0.9;

            if ((oldLeft - scaleX * (newWidth - oldWidth)) < 500 && (oldLeft - scaleX * (newWidth - oldWidth)) > -400) {
                this.style.left = oldLeft - scaleX * (newWidth - oldWidth) + "px";
                this.style.top = oldTop - scaleY * (newHeight - oldHeight) + "px";
            }
        }

        oldWidth = oldWidth * 0.9 + 2;
        oldHeight = oldHeight * 0.9 + 2;

    } else {
        if (zoom < 1.8) {
            zoom *= 1.21;
            this.style.zoom = zoom;

            var newWidth = oldWidth * 1.1;
            var newHeight = oldHeight * 1.1;
            if ((oldLeft - scaleX * (newWidth - oldWidth)) < 500 && (oldLeft - scaleX * (newWidth - oldWidth)) > -400) {
                this.style.left = oldLeft - scaleX * (newWidth - oldWidth) + "px";
                this.style.top = oldTop - scaleY * (newHeight - oldHeight) + "px";
            }

        }
        oldWidth = oldWidth * 1.1 + 2;
        oldHeight = oldHeight * 1.1 + 2;
    }
});

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
addLoadEvent(moveMouse);
addLoadEvent(initDrag);