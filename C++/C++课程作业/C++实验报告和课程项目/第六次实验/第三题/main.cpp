//
//  main.cpp
//  three6
//
//  Created by Worlder on 2018/12/31.
//  Copyright © 2018 Worlder. All rights reserved.
//

#include <iostream>
#include <vector>
#include <list>
#include "test.h"
using namespace std;

int main()
{
    int array_a[] = {11, 12, 13, 14, 15, 16, 17, 18, 19, 20};
    vector<int> vec_a(array_a, array_a + 10);
    list<int> list_a(array_a, array_a + 10);
    
    cout << "未执行函数的数组：" << endl;
    for (int i : array_a) //输出原来的数组
    {
        cout << i << "  ";
    }
    cout << "Median: " << median<int>(array_a, array_a + 10) << endl;
    cout << "执行函数后的数组：" << endl;
    for (int i2 : array_a) //输出原来的数组
    {
        cout << i2 << "  ";
    }
    
    cout << endl
    << "未执行函数的向量：" << endl;
    for (auto &j : vec_a)
    {
        cout << j << "  ";
    }
    cout << "Median: " << median<int>(vec_a.begin(), vec_a.end()) << endl;
    cout << "执行函数后的向量：" << endl;
    for (auto &j2 : vec_a)
    {
        cout << j2 << "  ";
    }
    
    cout << endl
    << "未执行函数的list：" << endl;
    for (auto &k : list_a)
    {
        cout << k << "  ";
    }
    cout << "Median: " << median<int>(list_a.begin(), list_a.end()) << endl;
    cout << "执行函数后的list：" << endl;
    for (auto &k2 : list_a)
    {
        cout << k2 << "  ";
    }
    
    cout << endl;
    
    return 0;
}
