#include <iostream>
#include <string>

using namespace std;

int main()
{
    string text;
    string s;
    char temp;

    while (cin.get(temp))
    {
        if (temp == '\t')
        {
            string str;
            cin >> str;
            text += ' ' + str;
        }
        else if (temp == ' ')
        {
            string str;
            cin >> str;
            text += ' ' + str;
        }
        else if (temp == '\n')
            cin.ignore(1, EOF);
        else
            text += temp;
    }

    s = text;
    for (string::size_type i = 0; i < s.size(); i++)
        if (s[i] <= 'Z' && s[i] >= 'A')
            s[i] += 'a' - 'A';
    int pos = s.find("bullshit", 0);

    for (string::size_type j = 0; j < text.size(); j++)
    {
        if (text[j] <= 'Z' && text[j] >= 'A')
            text[j] += 'a' - 'A';
        else if (text[j] <= 'z' && text[j] >= 'a')
            text[j] -= 'a' - 'A';
    }
    if (pos > 0)
    {
        text.replace(pos, 8, "bush");
    }
    cout << text << '\n';

    return 0;
}
