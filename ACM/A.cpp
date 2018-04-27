#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
    int a[8];
    a[0] = 1;
    a[1] = 2;
    a[2] = 0;
    a[3] = 2;
    a[4] = 2;
    a[5] = 1;
    a[6] = 0;
    a[7] = 1;
    int n;
    while(cin>>n)
    {
        if(a[n%8]==0)
            printf("yes\n");
        else
            printf("no\n");
    }
}