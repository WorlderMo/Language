#include <iostream>
#include <string>

using namespace std;

int main(int argc, char const *argv[])
{
    cout << "Please enter your first name:" << '\n';

    // 读取姓名
    string name;
    cin >> name;

    const string greeting = "Hello, " + name + "!";

    //问候语周围的空白数量
    const int pad = 1;

    //要写入的行数和列数
    const int rows = pad * 2 + 3;
    const string::size_type cols = greeting.size() + pad * 2 + 2;
    const string spaces = string(greeting.size() + pad * 2, ' ');

    cout << endl;

    //输出行
    for (int r = 0; r != rows; ++r)
    {
        string::size_type c = 0;
        while (c != cols)
        {
            if (r == pad + 1 && c == pad + 1)
            {
                cout << greeting;
                c += greeting.size();
            }
            else
            {
                // 是否处于边界
                if (r == 0 || r == rows - 1 ||
                    c == 0 || c == cols - 1)
                {
                    cout << "*";
                    ++c;
                }
                else if (r == pad + 1)
                {
                    cout << " ";
                    ++c;
                }
                else
                {
                    cout << spaces;
                    c += spaces.size();
                }
            }
        }

        cout << endl;
    }

    return 0;
}
