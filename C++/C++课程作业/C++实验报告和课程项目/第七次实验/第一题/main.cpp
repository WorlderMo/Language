//
//  main.cpp
//  one7
//
//  Created by Worlder on 2018/12/31.
//  Copyright © 2018 Worlder. All rights reserved.
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
    cout << "删除首元素之后的vector：" << endl;
    Vec<string>::iterator it = test.begin();
    it = test.erase(it);
    for (; it != test.end(); ++it)
    {
        cout << (*it) << "    ";
    }
    cout << endl
    << "将整个vector清空之后的vector：" << endl;
    test.clear();
    for (auto it2 = test.begin(); it2 != test.end(); ++it2)
    {
        cout << "*it2"
        << "    ";
    }
    return 0;
}

