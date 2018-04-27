#include <iostream>
#include <string>

//声明我们使用的标准库名称
using std::cin; using std::cout;
using std::endl; using std::string;

int main(int argc, char const *argv[])
{
    //请求用户输入姓名
    cout << "请输入你的名字：";
    string name;
    cin >> name;

    //构造我们将要输出的信息
    const string greeting = "Hello, " + name + "!";

    //围住问候语的空白个数
    const int pad = 1;

    //待输出的行数和列数
    const int rows = pad * 2 + 3;
    const string::size_type cols = greeting.size() + pad * 2 + 2;

    //输出一个空白行，将输出和输入分隔开
    cout << endl;

    //输出rows行
    //不变式：到目前为止，我们已经输出r行
    for(int r=0; r != rows; ++r)
    {
        string::size_type c = 0;

        //不变式：到目前为止，我们已经在当前行输出了c个字符
        while (c != cols)
        {
            //是否应该输出问候语了？
            if (r == pad + 1 && c == pad + 1)
            {
                cout << greeting;
                c += greeting.size();
            }
            else
            {
                //我们是否位于边界上？
                if (r == 0 || r == rows - 1 || c == 0 || c == cols - 1)
                    cout << "*";
                else
                    cout << " ";
                ++c;
            }
        }
            cout << endl;
    }
    return 0;
}
