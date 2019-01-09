//
//  test.h
//  three6
//
//  Created by Worlder on 2018/12/31.
//  Copyright © 2018 Worlder. All rights reserved.
//

#ifndef test_h
#define test_h

#include <algorithm>
#include <stdexcept>
#include <vector>

using namespace std;
template <class T, class p>
T median(p begin, p end)
{
    if (begin == end)
        throw domain_error("median of an empty container");
    
    vector<T> temp;
    for (; begin != end; ++begin) //无论是什么类型的容器，都将其插入临时向量temp中
        temp.push_back(*begin);
    sort(temp.begin(), temp.end());
    
    size_t mid = temp.size() / 2;
    return (temp.size() % 2 == 0) ? (temp[mid] + temp[mid - 1]) / 2 : temp[mid];
}

#endif /* test_h */
