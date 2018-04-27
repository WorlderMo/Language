#include <iostream>
#include <string>

int main(int argc, char const *argv[])
{
    std::cout << "请输出你的名字：";
    std::string name;
    std::cin >> name;

    //构造我们将要输出的信息
    const std::string greeting = "Hello," + name + "!";

    //构建输出的第二行和第四行
    const std::string spaces(greeting.size(), ' ');
    const std::string second = "*" + spaces + "*";

    //构建输出的第一行和第五行
    const std::string first(second.size(), '*');

    //输出全部内容
    std::cout << std::endl;
    std::cout << first << std::endl;
    std::cout << second <<std::endl;
    std::cout << "*" << greeting << "*" << std::endl;
    std::cout << second << std::endl;
    std::cout << first << std::endl;
    return 0;
}
