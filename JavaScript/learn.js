"use strict"; // 这个语句声明使用 JavaScript 严格模式

/*************************
    JavaScript基本语法
*************************/

//建议每个语句后面都加“;”
//声明变量
var variable = 1;
//也可不用声明，直接创建变量，类似于Python
variable = 1;
// 无穷大：Infinity; 负无穷大：-Infinity
// 非数字值：NaN

// 字符串
// 具有 length属性
var str = "mohailang";
var len = str.length;
// parseInt()可以把字符串里的数值信息提取出来(parseFloat())
var intNum = parseInt("520ssss"); // 会提取出520这个数值返回给 intNum
// 在字符串中查找字符串: 字符串使用 indexOf() 来定位字符串中某一个指定的字符首次出现的位置
var n = str.indexOf("hailang");
// match()函数用来查找字符串中特定的字符，并且如果找到的话，则返回这个字符。
var str1 = str.match("lang");
// replace() 方法在字符串中用某些字符替换另一些字符。
var str2 = str.replace("hailang", "nuonuo");
// 字符串大小写转换使用函数 toUpperCase() / toLowerCase():
var str3 = str.toLowerCase();
var str4 = str.toUpperCase();
// 字符串使用split()函数转为数组
var mystr = "mo,hai,lang";
var myarray = mystr.split(",");

//创建数组
var array = Array();
//或者
var array = new Array();
//或者:类似于Python的列表
var array = [];
// 当使用关联数组的时候，数组的方法和属性就不能再使用，否则会产生错误
array["a"] = "aaa";
array["b"] = "bbb";
var n = array.length; // n的值只会是数组正常索引的个数，不会加上使用名字来索引的个数
// 创建数组的新方法
Array.prototype.myUcase = function () {
    for (let i = 0; i < this.length; i++) {
        this[i] = this[i].toUpperCase();
    }
};
var array1 = ["a", "b", "c"];
array1.myUcase(); //调用新增的方法
// 合并两个数组
var array2 = ["d", "e"];
var sumArray = array1.concat(array2);
// 其他方法：join()、pop()、push()、reverse()


//创建对象
var object = Object();
//或者：类似于Python的字典
var object = {
    name: "mohailang",
    methodName: function () {
        return this.name;
    }
};
name = object.name;
name = object["name"];
object.methodName(); // 调用对象方法


// 操作符：可以使用++
variable++;
// + 也作为拼接符
var string = "mo" + "hailang";


// 函数变量的作用域：
// 如果在某个函数中使用了 var声明变量,那个变量就将视为一个局部变量，否则就视为一个全局变量
// let声明的变量只在其声明的块或者字块中可用，而 var的作用是整个封闭函数
// 用 window 全局对象来声明一个全局变量：window.var
function myfunction(a, b) {
    var x = 1; // 作用域为 myfunction
    if (true) {
        let x = 2; // 和前一个 x 是不同的变量，作用域只在 if 语句块中
    }
    return a * b;
}
// 函数也可以通过一个表达式来定义
var fun = function (a, b) {
    return a * b;
};
var z = fun(4, 3);
// 匿名函数
var fun = function () {
    console.log("匿名函数");
};
// 也可以自调用函数
(function () {
    var x = "自我调用"; // 函数将调用自身
})(); // 通过添加括号，来说明它是一个函数表达式
// arguments.length 属性返回函数调用过程接收到的参数个数：
// argument 对象包含了函数调用的参数数组。
function myFunction(a, b) {
    return arguments.length;
}
//toString() 方法将函数作为一个字符串返回:
function myFunction(a, b) {
    return a * b;
}
var txt = myFunction.toString();

// 一般而言，在Javascript中，this指向函数执行时的当前对象。

// 也可以使用构造函数来调用函数
// 构造函数:可以用来实例化一个对象
function myFunction(arg1, arg2) {
    this.firstName = arg1;
    this.lastName = arg2;

    function changeName(name) {
        this.lastName = name;
    }
    this.changeName = changeName;
}
// This 创建了新的对象
var x = new myFunction("John", "Doe");
x.firstName; // 返回 "John"

// 也可以作为函数方法使用 call()或者 apply()来调用函数

// 内建对象Array、Date、Math
// 宿主对象：有浏览器提供的预定义对象，比如 document 对象


// 输出:
// 1.弹出警告框
window.alert();
// 2.将内容写入到 HTML 文档中
document.write();
// 3.向指定id的元素输出文本
document.getElementById().innerHTML = "text";
// 写入到浏览器的控制台
console.log();


// 字符串也可以使用索引，从[0]开始
var mystring = "mohailang";
a = mystring[2];
// 使用内置属性 length来计算字符串的长度
var len = mystring.length;
// ==是值相等，===是值和类型都相等
// 条件运算符(三目运算符）: "?:"


// JavaScript 可以使用 switch 语句
switch (key) {
    case value:
        break;

    case 1:
    case 2:
        alert("1 or 2"); //当两种情况相同时，可以只在第二种情况中写要执行的代码

    default:
        break;
}

// JavaScript 也可以使用 for/in 循环
// 但 JavaScript 并不是直接遍历对象的值，而是遍历它的索引或者键，与 Python 的不一样
var array = [2, 1, 4, 7, 9];
for (const key in array) { // key的值并不是 array 中的值，而是索引值0，1，2，3，4
    if (array.hasOwnProperty(key)) {
        const element = array[key];
        console.log(element);
    }
}

// break 语句用于跳出循环。
// continue 用于跳过循环中的一个迭代,直接开始下一个迭代
// JavaScript标签：通过标签引用，break 和 continue 可以跳出 JavaScript 代码块，但 continue 只能用在循环中


// 可以使用 typeof 操作符来检测变量的数据类型
typeof "mohailang"; // 返回 string
// instanceof 操作符用来判断对象的具体类型
arr = [1, 2, 3];
if (arr instanceof Array) {
    console.log("arr 是一个数组");
}
// null 和 undefined的值相等，但类型不同


// Number() 转换为数字， String() 转换为字符串， Boolean() 转化为布尔值。
// constructor 属性返回所有 JavaScript 变量的构造函数。
a = new Date().constructor; // 返回函数 Date
a = function () {}.constructor; // 返回函数 Function
// 可以使用 constructor属性来查看对象是否为数组（包含字符串“Array”）
function isArray(myArray) {
    return myArray.constructor.toString.indexOf("Array") > -1;
}


// + 可用于将变量转换为数字
var y = "2222"; // y是一个字符串
var x = +y; // x 是一个数字


// 正则表达式：/正则表达式主体/修饰符(可选)
var pattern = /hailang/i
// hailang  是一个正则表达式主体 (用于检索)。
// i 是一个修饰符(搜索不区分大小写) 。
// search() 方法 用于检索字符串中指定的子字符串，或检索与正则表达式相匹配的子字符串，并返回子串的起始位置。
// replace() 方法 用于在字符串中用一些字符替换另一些字符，或替换一个与正则表达式匹配的子串,返回修改后的字符串，但并不修改原字符串
var str = "mohailang"
var n = str.search(/lang/i)
var n = str.search("lang")

var txt = str.replace(/hailang/i, "lang"); // txt为“molang”,但 str仍为“mohailang”

// test() 方法用于检测一个字符串是否匹配某个模式，如果字符串中含有匹配的文本，则返回 true，否则返回 false。
/lang/.test(str);

// exec() 方法用于检索字符串中的正则表达式的匹配。该函数返回一个数组，其中存放匹配的结果。如果未找到匹配，则返回值为 null.
/lang/.exec(str)

// 也可以直接创建一个 RegExp 对象
var pattern = new RegExp("lang") // 此时 pattern等同于 /lang/


// try-throw-catch
try {
    if (1 < 2) {
        throw "1<2";
    }
} catch (error) { // error 为throw抛出的错误
    console.log(error);
}


// void操作符：只执行表达式，但没有返回值：javascript：void (表达式)
// href="#": #包含了一个位置信息，默认的锚是#top 也就是网页的上端。


/*************************
    JavaScript HTML DOM
*************************/

// HTML-DOM中，元素对象可以直接通过 "."来操作属性
var srcvalue = element.src;

// 当页面被加载时，浏览器会创建页面的文档对象模型（Document Object Model）

// 1. 通过 id 查找 HTML元素,返回的该元素的对象形式
var x = document.getElementById("elementId");
// 2. 通过标签名查找 HTML 元素
var y = x.getElementByTagName("p"); // 查找指定 ID 下的所有<p>元素
// 3. 通过类名找到 HTML元素
var x = document.getElementsByClassName("classNames");
// 得到需要的元素后，就可以使用getAttribute()来获取它的各个属性，用 setAttribute()来更改各个属性
var z = x.getAttribute("title");


// 改变 HTML
// 1. 改变 HTML输出流
document.write("输出");
// 2. 改变 HTML内容
document.getElementById("elementId").innerHTML = "text";
// 3. 改变 HTML属性
document.getElementById("image").src = "mohailang.jpg";


// 改变 CSS: document.getElementById(id).style.property=新样式


// JavaScript HTML DOM事件
// 往一个 HTML事件属性添加 JavaScript 代码：onclick=JavaScript
// 使用 HTML DOM来分配事件
document.getElementById("elementId").onclick = function () {
    myfunction(a, b);
}; // myfunction被分配给指定 ID 的 HTML 元素
// onload 和 onunload 事件会在用户进入或离开页面时被触发。
// onchange 事件:对于输入当鼠标离开这个事件或者按下 enter 键后，onchange对应的 JavaScript 就会执行，常用来对输入字段进行验证


// JavaScript HTML DOM EventListener
// 触发监听事件：向指定的元素添加事件句柄
document.getElementById("elementId").addEventListener("click", myfunction);
// 当传递参数值时，需要使用匿名函数来调用带参数的函数：
document.getElementById("elementId").addEventListener("click", function () {
    myfunction(a, b);
});
// 事件冒泡或事件捕获
// 在冒泡中，内部元素的事件会先被触发，然后再触发外部元素
// 在捕获中，外部元素先被触发，然后才会触发内部元素
// 默认值为 false，即冒泡传递，当值为 true 时，事件使用捕获传递
document.getElementById("elementId").addEventListener("click", myfunction, true);
// removeEventListener() 方法移除由 addEventListener() 方法添加的事件句柄
document.getElementById("elementId").removeEventListener("click", myFunction);


// JavaScript HTML DOM 元素 (节点)
// 要创建新的 HTML 元素 (节点)需要先创建一个元素，然后在已存在的元素中添加它。
// 1. appendChild()用于将新元素添加到尾部
var para = document.createElement("tagName"); // 创建元素节点
var node = document.createTextNode("这是一个新的text"); // 为元素添加文本节点
para.appendChild(node); // 为元素添加文本节点
var element = document.getElementById("elementId"); // 查找已存在的节点
element.appendChild(para); // 添加到已存在的节点
// 2. insertBefore()用于将新元插入到现有元素的前面
var targetElement = document.getElementById("elementId"); // 查找原来的开始位置的元素
targetElement.parentNode.insertBefore(newElement, targetElement);
// 编写 insertAfter函数
function insertAfter(newElement, targetElement) {
    var parent = targetElement.parentNode;
    if (parent.lastChild == targetElement) {
        parent.appendChild(newElement);
    } else {
        parent.insertBefore(newElement, targetElement.nextSibling);
    }
}
// removeChild()移除已存在的元素(需要知道父元素)
// 父元素都可以通过 parentNode获得
element.removeChild(child);
// 或者：
child.parentNode.removeChild(child);
// replaceChild()替换 HTML元素
element.replaceChild(para, child);

// childNodes属性获取任何一个元素的所有子元素，不包含属性节点
var elements = element.childNodes;
// nodeType 属性：获取节点的类型
// 元素节点的 nodeType 属性值是1
// 属性节点的 nodeType 属性值是2
// 文本节点的 nodeType 属性值是3
var type = element.nodeType;
// nodeValue 属性：用来获取或者设置一个节点的值
// 比如想获取<p id="description">choose a image.</p>中的文本值
var description = document.getElementById("description");
var value = description.childNodes[0].nodeValue;
// 元素节点的子节点不包含属性节点，因为元素节点本身包包含了属性节点
// firstChild和 lastChild 属性：分别代表着 childNodes的第一个元素和最后一个元素
var value = description.firstChild.nodeValue; // 等同于var value=description.childNodes[0].nodeValue;
// nodeName 属性：节点的名称，比如<p>节点的 nodeName 就是是 p
// 元素节点的下一个节点(同级节点，而不是子节点)可以使用nextSibling 来获得
var nextElement = element.nextSibling

// JavaScript HTML DOM 集合(Collection)
// getElementsByTagName() 方法返回 HTMLCollection 对象。
// 类似于数组，具有 length 属性，可以用索引(包括name,id)来获取元素，但没有数组的其他属性
var x = document.getElementsByTagName("tagname");

// JavaScript HTML DOM 节点列表: NodeList 对象是一个从文档中获取的节点列表 (集合) 。
// NodeList 对象类似 HTMLCollection 对象,但只能使用索引来获取元素
var myNodeList = document.querySelectorAll("selectors");


/********************
 * BOM 浏览器对象模型
 *******************/

// Window、Window Screen、Window Location、Window History、Navigator

// 网页加载完毕时会触发一个 onload 时间，这个事件与 window 对象相关联
// 绑定 JavaScript 函数到 onload 事件处理函数中
function addLoadEvent(func) {
    var oldonload = window.onload;
    if (typeof window.onload != 'function') {
        window.onload = func;
    } else {
        window.onload = function () {
            oldonload();
            func();
        };
    }
}
// JavaScript 弹窗(三者都可以不带上window对象)
// 1. 警告框
window.alert("警告");
// 2. 确认框
window.confirm("确认");
// 3. 提示框
window.prompt("请输入你的名字", "mohailang");

// 创建新的窗口
// URL: 打开新窗口的 URL 地址
// windowName: 新窗口的名字
// feature：新窗口的各种属性，以字符串形式
window.open(URL, windowName, feature);

// "javascript:"伪协议：通过一个连接来调用 JavaScript 函数
{ /* <a href="javascript:function()">伪协议</a> */ }
// 使用伪协议的做法并不好

// JavaScript计时事件
// setInterval()间隔指定的毫秒数不停地执行指定的代码，第一个参数时函数，第二个参数时间隔的毫秒数
var myVar = window.setInterval(function () {
    alert("Hello");
}, 3000); // 可省略 window 对象
// clearInterval() 方法用于停止 setInterval() 方法执行的函数代码。
window.clearInterval(myVar);

// setTimeout()方法：setTimeout() 的第一个参数是含有 JavaScript 语句的字符串。这个语句可能诸如 "alert('5 seconds!')"，或者对函数的调用，诸如 alertMsg。第二个参数指示从当前起多少毫秒后执行第一个参数。
var myVar = window.setTimeout(function () {
    alert("Hello");
}, 3000);
// clearTimeout() 方法用于停止执行setTimeout()方法的函数代码
clearTimeout(myVar);


// JavaScript Cookie: Cookie 用于存储 web 页面的用户信息。
var x = document.cookie;
// JavaScript可以对 cookie进行创建、读取、修改、删除、


// JavaScript的一些简单有用的实例：http://www.runoob.com/js/js-examples.html


// 可以对 JavaScript 脚本进行压缩，精简副本在文件名中加上 min 字样



/**************
 *  Ajax
 *************/

// XMLHttpRequest用于在后台和服务器交换数据

// 对象检测
var xmlhttp;
if (window.XMLHttpRequest) {
    // 所有现代浏览器创建 XMLHttpRequest对象
    xmlhttp = new XMLHttpRequest();
} else {
    // IE5,IE6浏览器创建 ActiveX对象
    xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
}

// 使用 XMLHttpRequest对象的 open()和 send()来将请求发送到服务器
xmlhttp.open(method, url, async);
// method: GET 请求或者 POST请求
// url:服务器上的文件
// async: true(异步)、false(同步)
xmlhttp.send("string"); // string仅用于 POST请求

// 使用 XMLHttpRequest对象的 responseText 或者 responseXML 属性来获得来自服务器的响应
// responseText 属性：获得字符串形式的响应数据
// responseXML 属性：获取 XML 形式的响应格式
var text = xmlhttp.responseText;
var xml = xmlhttp.responseXML;

// onreadystatechange 是事件处理函数，他会在服务器给 XMLHttpRequest对象送回响应的时候被触发执行
// onreadystatechange:存储函数，每当 readyState 属性改变时，就会调用该函数
// readyState:存有 XMLHttpRequest的状态，从0到4发生变化
// 0:请求未初始化；1：服务器连接已建立；2：请求已接收；3：请求处理中；4：请求已完成，且响应已就绪。
// status: 200:"OK"; 404:未找到页面
xmlhttp.onreadystatechange = function () {
    // 当 readyState==4且 status==200时，表示响应已就绪
    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
        document.getElementById("elementId").innerHTML = xmlhttp.responseText;
    }
};

// 回调函数：回调函数是一个作为变量传递给另外一个函数的函数，它在主体函数执行完之后执行
// function A 有一个一个参数function B,function B 会在function A 执行完之后被调用执行`

// hijax: 渐进增强的 ajax


// 改变 CSS 样式
// 当需要使用一个中间带减号的 CSS 属性（font-family）的时候，DOM 要求用驼峰命名法(fontFamily)
// 利用 style 属性检测出元素的样式
var color = element.style.color;
// 也可以修改元素的样式
element.style.fontFamily = "Times";
// 通过 className属性得到一个元素的 class 属性
var classAttr = element.className;
// 改变样式最好选择去更新 className属性，而不是去直接更新 style 对象的有关属性


// 用 JavaScript实现动画效果
// setTimeout 能够让某个函数经过一段预定的时间之后才开始执行
variable = setTimeout(handler, timeout);
// 取消等待队列中的某个函数
clearTimeout(variable);
