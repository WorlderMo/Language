#include <iostream>
#include <stdio.h>
using namespace std;
class X
{
　　public:virtual void f(){ cout<<"aa\n";}
};
class Y:public X
{
public:void f(){ cout<<"bb\n";}
};

int main(void)
{
　　int a=1;
    float b=2.0;
    int c=a+b;
    printf('%d',c);
    return 0;
}
