//
//  main.cpp
//  three7
//
//  Created by Worlder on 2019/1/1.
//  Copyright © 2019 Worlder. All rights reserved.
//

#include <iostream>
#include "str.h"
#include "Vec.h"
using namespace std;

int main()
{
    str a, b;
    cout << "请输入需要比较的字符串：" << endl;
    cin >> a >> b;
    
    if (a != b)
    {
        cout << "a!=b" << endl;
        if (a > b)
            cout << "a>b" << endl;
        else
            cout << "a<b" << endl;
    }
    else
        cout << "a=b" << endl;
    
    return 0;
}

