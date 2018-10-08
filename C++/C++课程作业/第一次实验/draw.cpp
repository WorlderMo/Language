#include <iostream>
using namespace std;

int main()
{
    const int rows = 16;
    const int cols = 52;
    int r, c;
    for (r = 0; r != rows; ++r)
    {
        c = 0;
        while (c != cols)
        {
            if (r == 0 || r == rows - 1 || c == 0 || c == cols - 1)
            {
                cout << "*";
                ++c;
            }
            else if (r == 4)
            {
                if (c >= 4 && c <= 12)
                {
                    cout << "*";
                    ++c;
                }
                else if (c == 20)
                {
                    cout << "*";
                    ++c;
                }
                else if (c >= 28 && c <= 36)
                {
                    cout << "*";
                    ++c;
                }
                else if (c >= 40 && c <= 48)
                {
                    cout << "*";
                    ++c;
                }
                else
                {
                    cout << " ";
                    ++c;
                }
            }
            else if (r == 5)
            {
                if (c == 16 && c == 24)
                {
                    cout << "*";
                    ++c;
                }
                else if (c == 4 || c == 8 || c == 12 || c == 20 || c == 32 || c == 44)
                {
                    cout << "*";
                    ++c;
                }
                else
                {
                    cout << " ";
                    ++c;
                }
            }
            else if (r == 6)
            {
                if (c >= 16 && c <= 24)
                {
                    cout << "*";
                    ++c;
                }
                else if (c == 4 || c == 8 || c == 12 || c == 20 || c == 32 || c == 44)
                {
                    cout << "*";
                    ++c;
                }
                else
                {
                    cout << " ";
                    ++c;
                }
            }
            else if (r == 7)
            {
                if (c == 16 || c == 24)
                {
                    cout << "*";
                    ++c;
                }
                else if (c == 4 || c == 8 || c == 12 || c == 20 || c == 32 || c == 44)
                {
                    cout << "*";
                    ++c;
                }
                else
                {
                    cout << " ";
                    ++c;
                }
            }
            else if (r == 8)
            {
                if (c >= 16 && c <= 24)
                {
                    cout << "*";
                    ++c;
                }
                else if (c >= 4 && c <= 12)
                {
                    cout << "*";
                    ++c;
                }
                else if (c == 29 || c == 32 || c == 33 || c == 35 || c == 34 || c == 36)
                {
                    cout << "*";
                    ++c;
                }
                else if (c == 44 || c == 46)
                {
                    cout << "*";
                    ++c;
                }
                else
                {
                    cout << " ";
                    ++c;
                }
            }
            else if (r == 9)
            {

                if (c == 4 || c == 8 || c == 12 || c == 20 || c == 29 || c == 32 || c == 44 || c == 47)
                {
                    cout << "*";
                    ++c;
                }
                else
                {
                    cout << " ";
                    ++c;
                }
            }
            else if (r == 10)
            {
                if (c == 4 || c == 8 || c == 12 || c == 20 || c == 29 || c == 32 || c == 44 || c == 48)
                {
                    cout << "*";
                    ++c;
                }
                else
                {
                    cout << " ";
                    ++c;
                }
            }
            else if (r == 11)
            {
                if (c == 4 || c == 8 || c == 12 || c == 20 || c == 29 || c == 32 || c == 44)
                {
                    cout << "*";
                    ++c;
                }
                else
                {
                    cout << " ";
                    ++c;
                }
            }
            else if (r == 12)
            {
                if (c >= 4 && c <= 12)
                {
                    cout << "*";
                    ++c;
                }
                else if (c == 20 || c == 44)
                {
                    cout << "*";
                    ++c;
                }
                else if (c >= 28 && c <= 36)
                {
                    cout << "*";
                    ++c;
                }
                else
                {
                    cout << " ";
                    ++c;
                }
            }
            else
            {
                cout << " ";
                ++c;
            }
        }
        cout << endl;
    }
    return 0;
}
