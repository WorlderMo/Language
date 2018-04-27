#include <iostream>
int main(int argc, char const *argv[])
{
    using namespace std;
    char ch;
    int spaces = 0;
    int total = 0;
    cin.get(ch);
    while (ch != '.')
    {
        if (ch == ' ')
            ++spaces;
        ++total;
        cin.get(ch);
    }
    cout << spaces << " spaces " << total;
    cout << " characters tatal in sentence\n"
         << endl;
    return 0;
}
