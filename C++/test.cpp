#include<iostream>
using namespace std;
class A{
public:
     virtual  void  display(){  cout<<"A"<<endl; }
     };
class B :  public A{
public:
            void  display(){ cout<<"B"<<endl; }
     };
void doDisplay(A *p)
{
    p->display();
    delete p;
}

int main(int argc,char* argv[])
{
    doDisplay(new B());
    return 0;
}
