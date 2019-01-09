#include <iostream>
#define LEN 10
int main(int argc, char const *argv[])
{
    // sizeof 检查电脑各种数据类型的大小
    // typedef声明 为一个已有类型取一个新的名字
    // 枚举类型 enum 变量取值有限，可以一一枚举,都比前一个要大1
    enum color
    {
        red, // 相当于一个变量名，值为0
        green = 4,
        blue //5
    };
    // 在函数内，局部变量的值会覆盖全局变量的值
    // 当局部变量被定义时，系统不会对其初始化，必须自行对其初始化。定义全局变量时，系统会自动初始化为对应的零值
    // 定义常量: 使用 #define 预处理器 或者使用 const 关键字,一般都为答谢形式
    const int LENGTH = 10;
    // 修饰符 signed、unsigned、long 和 short 可应用于整型，signed 和 unsigned 可应用于字符型，long 可应用于双精度型。
    // 修饰符 signed 和 unsigned 也可以作为 long 或 short 修饰符的前缀。例如：unsigned long int。

    // static存储类：指示编译器在程序的生命周期内保持局部变量的存在，而不需要在每次它进入和离开作用域时进行创建和销毁
    return 0;
}
