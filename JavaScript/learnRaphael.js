/*
 * @Author: mohailang (1198534595@qq.com)
 * @Date: 2018-08-04 20:29:51
 * @Last Modified by: mohailang
 * @Last Modified time: 2018-08-08 14:50:29
 */

// 实例化画板
var paper = new Raphael(element, width, height); // 或者直接传递元素的 ID 作为参数
// 然后再画板上绘制各种图形

// 绘制图形
var circle = paper.circle(cx, cy, r);

// 绘制椭圆形
var ellipse = paper.ellipse(cx, cy, rx, ry);

// 绘制矩形
var rectangle = paper.rect(x, y, width, height);

// 加载图片
var img = paper.image("photo", x, y, width, height);

// 文字
var text = paper.text(x, y, "text");

// 绘制 path 路径
var path = paper.path('M10,30 L60,30 L10,80 L60,80');

// 为图形添加属性
circle.attr("fill", "red");
