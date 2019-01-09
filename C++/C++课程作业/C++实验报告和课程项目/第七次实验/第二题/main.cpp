//
//  main.cpp
//  two7
//
//  Created by Worlder on 2018/12/31.
//  Copyright © 2018 Worlder. All rights reserved.
//

#include <iostream>
#include "list.h"

using namespace std;

int main()
{
    Lst<int> list;
    int a[5] = { 10,11,12,13,14 };
    for (int i = 0; i != 5; ++i)
    {
        list.push_back(a[i]);
    }
    Lst<int>::iterator it = list.begin();
    for (; it != list.end(); ++it)
    {
        cout << *it << "   ";
    }
    cout << endl;
    return 0;
}
