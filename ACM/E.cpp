#include <iostream>
using namespace std;
int main()
{
    long long n,k;
    while(cin>>n>>k)
    {
        long long sum=0,x;
        for(int i=0;i<n;i++)
        {
            cin>>x;
            sum+=(x+k-1)/k;
        }
        cout<<(sum+1)/2<<endl;
    }
    return 0;
}