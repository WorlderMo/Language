//
//  main.cpp
//  five7
//
//  Created by Worlder on 2019/1/1.
//  Copyright © 2019 Worlder. All rights reserved.
//

#include<iostream>
#include"Vec.h"
using namespace std;

int main()
{
    int a[5] = { 1,2,3,4,5 };
    Vec<int> copyA;
    copyA.assign(a, a+5);
    Vec<int>::iterator it = copyA.begin();
    for (;it!=copyA.end();++it)
    {
        cout << *it << "   ";
    }
    cout << endl;
    char c[5] = {'A','B','C','D','E'};
    Vec<char> copyC;
    copyC.assign(c,c+5);
    Vec<char>::iterator it2 = copyC.begin();
    for (; it2 != copyC.end(); ++it2)
    {
        cout << *it2 << "   ";
    }
    cout << endl;
    return 0;
}
