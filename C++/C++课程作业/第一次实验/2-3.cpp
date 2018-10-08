#include <iostream>
#include <string>

using namespace std;

int main()
{
    cout << "Please enter your first name: " << '\n';

    string name;
    cin >> name;

    const string greeting = "Hello, " + name + "!";

    // 问候语周围的空白数量
    cout << "Please enter pad: " << ;
    int pad;
    cin >> pad;

    // 要写入的行数和列数
    const int rows = pad * 2 + 3;
    const string::size_type cols = greeting.size() + pad * 2 + 2;

    cout << endl;

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
                if (r == 0 || r == rows - 1 ||
                    c == 0 || c == cols - 1)
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
