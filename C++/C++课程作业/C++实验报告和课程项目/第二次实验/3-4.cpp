#include <iostream>
#include <iomanip>
#include <ios>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
int main()
{
    cout << "请输入字符串:\n";
    string max;
    string min;
    string input;
    cin >> input;
    max = min = input;
    while (cin >> input)
    {
        if (input.size() > max.size())
            max = input;
        if (input.size() < min.size())
            min = input;
    }
    cout << "最长字符串为:" << max << endl;
    cout << "最短字符串为:" << min << endl;
    system("pause");
    return 0;
}
