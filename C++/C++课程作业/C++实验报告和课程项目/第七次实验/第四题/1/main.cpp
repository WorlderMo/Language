//
//  main.cpp
//  four7
//
//  Created by Worlder on 2019/1/1.
//  Copyright © 2019 Worlder. All rights reserved.
//

#include <iostream>
#include <string>
#include "vec.h"
using namespace std;

int main()
{
    
    Vec<string> test;
    cout << "请输入五个字符串：" << endl;
    for (int i = 0; i != 5; ++i)
    {
        string t;
        cin >> t;
        test.push_back(t);
    }
    test.insert(test.begin(), &test[3], test.end());
    for (Vec<string>::iterator i = test.begin(); i != test.end(); ++i)
    {
        cout << *i << "    ";
    }
    cout << endl;
}

