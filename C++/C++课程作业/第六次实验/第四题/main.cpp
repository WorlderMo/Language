//
//  main.cpp
//  three6
//
//  Created by Worlder on 2018/12/31.
//  Copyright © 2018 Worlder. All rights reserved.
//

#include <iostream>
#include <string>
#include "test.h"
using namespace std;

int main()
{
    String_list onelist;
    cout << "请输入五个字符串：" << endl;
    for (int i = 0; i != 5; ++i)
    {
        string t;
        cin >> t;
        onelist.push_back(t);
    }
    
    cout << "正序输出：" << endl;
    String_list::iterator it = onelist.begin();
    while (it != onelist.end())
    {
        cout << (*it) << endl;
        ++it;
    }
    
    cout << "逆序输出：" << endl;
    String_list::iterator it2 = onelist.end();
    --it2;
    while (it2 != onelist.begin())
    {
        cout << (*it2) << endl;
        --it2;
    }
    cout << (*it2);
    cout << endl;
}
