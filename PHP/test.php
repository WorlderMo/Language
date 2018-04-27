<?php
/**
 *
 * @authors mohailang (1198534595@qq.com)
 * @date    2018-03-05 17:19:56
 */

// 该笔记只是简单记录 PHP 与其他语言有所差别的地方，方便复习

declare (encoding = 'utf-8');
// namespace: 命名空间，必须在最开头

// php变量以$开头来定义，后面跟字母，数字，下划线
$str = "I learn PHP";
echo "$str\n";
// 来自 PHP 之外的变量（$_GET,$_POST 超全局数组）
// echo $_POST['password']
// echo $_GET['name'];  //在浏览器输入 localhost:8888/test.php?name=mohailang 即可显示
// 或者用 HTML 文件输入

// 常量，常量默认为大小写敏感。传统上常量标识符总是大写的。可选参数如果为 TRUE，则变量不区分大小写。默认为全局变量
define("FOO", "something");
define('FOO1', 'somethings', true);

// echo 输出字符串，字符串可以包含 HTML 标签
echo "<h2>PHP</h2>";
echo "hello<br>";
echo "world<br>";
// 引用赋值
$a = 1;
$b = &$a;
$a = 2;
echo "$b\n"; // $b 也会改变，因为是 $a 的引用

// 结合比较运算符 <=> : 当$a小于、等于、大于than $b时 分别返回一个小于、等于、大于0的integer 值。 PHP7开始提供
// 5<=>6 返回-1 因为5小于6
// 5<=>5 返回0 因为5等于5
// 5<=>4 返回1 因为5大于4

// NULL 合并操作符 ?? : 从左往右第一个存在且不为 NULL 的操作数。如果都没有定义且不为 NULL，则返回 NULL。PHP7开始提供
$a = NULL;
$c = 5;
$b = 9;
$x = $a ?? $b ?? $c;
echo "$x\n";

// 错误控制运算符 @ ：
// PHP 支持一个错误控制运算符：@ 。当将其放置在一个 PHP 表达式之前，该表达式可能产生的任何错误信息都被忽略掉
// @ 运算符只对表达式有效

// 执行运算符：反引号(```)
// PHP 将尝试将反引号中的内容作为 shell 命令来执行，并将其输出信息返回（即，可以赋给一个变量而不是简单地丢弃到标准输出）。使用反引号运算符```的效果与函数 shell_exec() 相同。
// 与其它某些语言不同，反引号不能在双引号字符串中使用。
// 反引号运算符在激活了安全模式或者关闭了 shell_exec() 时是无效的。

// 字符串运算符：
// 1.连接运算符(.): 连接左右字符串
$a = "ssss";
$b = "aaaa";
$c = $a . $b;
echo "$c\n";
// 2.连接赋值运算符(.=): 与 += 运算符一样

// 进制互相转换
// 只需要记住bin、oct、dec、hex就可以了，你要把a进制转为b进制，那就是ab()
echo ($a = decbin(10));
// PHP提供了一个真正实现爱咋转就咋转的函数：base_convert();
// base_convert() 该函数有三个参数
// string base_convert ( string $number , int $frombase , int $tobase )
// 举个例子：
$hexadecimal = '127'; //十进制
echo base_convert($hexadecimal, 10, 5); //转为五进制
echo "\n";

// PHP 中也有三元运算符(?:)
echo (2 > 1 ? "yes" : "no"), "\n";
// 自 PHP 5.3 起，可以省略三元运算符中间那部分。表达式 expr1 ?: expr3 在 expr1 求值为 TRUE 时返回 expr1，否则返回 expr3。

// global 关键字用于函数内访问全局变量
// static 关键字用于保留变量前一次被调用的值
function myTest() {
	static $a = 1;
	echo "$a\n";
	$a++;
}

myTest();
myTest();

// PHP定界符 <<<EOF: Heredoc技术，可用来输出大段的html和javascript脚本,类似于 python 的三引号技术
$a = "mohailang";
echo <<<EOF
    <h1>我的第一个标题</h1>
    <p>我的第一个段落</p>
    $a\n
EOF;

// var_dump() 函数返回变量的数据类型和值
var_dump(123);
var_dump("123");

// 数组 array，类似于 python 的数组和字典的结合体
// count() 函数用于返回数组的长度（元素的数量）
// 完整的 PHP Array 参考手册: http://www.runoob.com/php/php-ref-array.html
$arrayName = array('mo' => "1", "hailng");
count(arrayName);

// strlen() 函数返回字符串的长度（字符数）
echo strlen("mohailang");
// strpos() 函数用于在字符串内查找一个字符或一段指定的文本，返回第一个匹配的字符位置
echo strpos("Hello world", "world");
// 完整的字符串函数参考网站 http://www.runoob.com/php/php-ref-string.html

// PHP7+ 版本新增整除运算符 intdiv()
var_dump(intdiv(10, 3));

// 组合比较符 <=>:
$c = $a <=> $b;
// 如果$a > $b, $c 的值为1
// 如果$a == $b, $c 的值为0
// 如果$a < $b, $c 的值为-1

// foreach 循环
foreach ($array as $key => $value) {
	# code...
}
$x = array("one", "two", "three");
foreach ($x as $value) {
	echo $value . " ";
}

// 函数 function
function functionName($variable) {
	// 要执行的代码
}

// PHP的对象需要通过 new 关键字来实例化，通过 -> 调用成员变量或者方法
// PHP_EOL 为换行符
// 构造函数：void __construct ([ mixed $args [, $... ]] )
// 析构函数：void __destruct ( void )

// 继承：PHP 使用关键字 extends 来继承一个类，PHP 不支持多继承，格式如下：
class Child extends Parent {
   // 代码部分
}

// 方法的重写：直接在子类对父类相同的方法进行改写，对父类方法进行覆盖
// 访问控制：与 java 的类似

// 接口：使用接口（interface），可以指定某个类必须实现哪些方法，但不需要定义这些方法的具体内容。接口是通过 interface 关键字来定义的
// 声明一个'iTemplate'接口
interface iTemplate
{
    public function setVariable($name, $var);
    public function getHtml($template);
}


// 实现接口
class Template implements iTemplate
{
    private $vars = array();

    public function setVariable($name, $var)
    {
        $this->vars[$name] = $var;
    }

    public function getHtml($template)
    {
        foreach($this->vars as $name => $value) {
            $template = str_replace('{' . $name . '}', $value, $template);
        }

        return $template;
    }
}
?>
