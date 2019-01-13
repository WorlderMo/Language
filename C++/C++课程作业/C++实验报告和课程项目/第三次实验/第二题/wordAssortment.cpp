#include <iostream>
#include <cstring>
#include <string>
#include <vector>
using namespace std;
int main()
{
    vector<string> vec1;
    vector<string> vec2;
    vector<string> vec3;
    string str;
    while (cin >> str)
    {
        if (isupper(str[0]) && islower(str[1]))
            vec2.push_back(str);
        else if (islower(str[0]))
            vec1.push_back(str);
        else
            vec3.push_back(str);
    }
    vector<string>::reverse_iterator r_it;
    cout << endl
         << "小写单词: ";
    for (r_it = vec1.rbegin(); r_it != vec1.rend(); r_it++)
        cout << *r_it << " ";

    cout << endl
         << "首字母大写: ";
    for (r_it = vec2.rbegin(); r_it != vec2.rend(); r_it++)
        cout << *r_it << " ";

    cout << endl
         << "大写单词: ";
    for (r_it = vec3.rbegin(); r_it != vec3.rend(); r_it++)
        cout << *r_it << " ";

    system("pause");
    return 0;
}
