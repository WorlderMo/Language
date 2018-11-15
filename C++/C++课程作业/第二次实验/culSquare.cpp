#include <iostream>
#include <iomanip>
using namespace std;
int nSize(int n)
{
    int k = 0;
    while (n > 0)
    {
        n /= 10;
        ++k;
    }
    return k;
}
int main()
{
    double f, n, k = 0;
    cout << "请输入I的值" << endl;
    cin >> n;
    for (double i = 1; i <= n; i = i + 1)
    {
        cout << setw(nSize(n) * 5) << setiosflags(ios::fixed) << setiosflags(ios::left) << setprecision(1) << i * i;
        cout << int(i) << endl;
    }

    return 0;
}
