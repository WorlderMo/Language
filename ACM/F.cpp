#include<stdio.h>
#include<algorithm>
#include<string>
#include<iostream>
using namespace std;
long long int m=1000000007;
int main()
{
    string s;
    cin>>s;
    int len=s.size();
    long long int ans=0;
    long long int sum=0;
    for(int i=len-1;i>=0;i--)
    {
        if(s[i]=='b')
        sum++;
        else if(s[i]=='a')
        {
            ans+=sum%m;
            ans%=m;
            sum*=2;
            sum%=m;
        }
    }
    printf("%d\n",ans%m);
    return 0;
}