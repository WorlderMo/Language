//
//  main.cpp
//  four5
//
//  Created by Worlder on 2018/12/31.
//  Copyright © 2018 Worlder. All rights reserved.
//

#include <iostream>
#include <string>
#include <iterator>
#include <vector>
#include <list>
#include <algorithm>

using namespace std;

int add6(int c)
{
    c += 6;
    return c;
}

bool p(int c)
{
    return c == 7;
}

//顺序只读迭代器
template <typename IN1, typename IN2>
bool find_equal(IN1 b1, IN1 e1, IN2 b2, IN2 e2)
{
    //遍历子串，若找到某个元素与原串中元素b1相同 则将原串与字串同时后移一位；
    //若没有，则返回false
    for (; b2 != e2 && b1 != e1; ++b2)
    {
        if (*b2 != *b1)
            return false;
        ++b1;
    }
    return true; //当退出循环时，即子串已被匹配完，返回true
}

template <typename IN1, typename IN2> //顺序只读迭代器
IN1 new_search(IN1 b1, IN1 e1, IN2 b2, IN2 e2)
{
    for (; b1 != e1; ++b1) //遍历原串
    {
        //若在子串中找到了全部子串所对应的字符串，返回子串第一个元素所处位置
        if (find_equal(b1, e1, b2, e2))
            return b1;
        //否则原串后移
    }
    return e1; //循环结束之后若if语句条件仍未成立，返回 e1
}

//顺序读写迭代器
template <typename InputIterator, typename outputIterator, typename function>
void new_transform(InputIterator b, InputIterator e,
                   outputIterator d, function f)
{
    for (; b != e; ++b)
    {
        *d++ = f(*b); //将迭代器所指内容用函数f替换 并存入迭代器d中
    }
    return;
}

//顺序只读迭代器
template <typename InputIterator, typename panduan>
InputIterator new_find_if(InputIterator b, InputIterator e, panduan p)
{
    for (; b != e; ++b)
    {
        if (p(*b))
            return b;
    }
    return e - 1;
}

//顺序读写迭代器
template <typename InputIterator, typename OutputIterator, typename panduan>
OutputIterator new_copy_if(InputIterator b, InputIterator e, OutputIterator d, panduan p)
{
    for (; b != e; ++b)
    {
        if (p(*b))
            *d++ = *b;
    }
    return d;
}

//顺序读写迭代器
template <typename InputIterator, typename panduan>
InputIterator new_partition(InputIterator b, InputIterator e, panduan p)
{
    InputIterator fail = b;
    for (; b != e; ++b)
    {
        if (p(*b))
            swap(*fail++, *b); //使谓词为真的元素被放入开头
    }
    return fail; //返回第一个不满足p元素所在的迭代器，如果都满足的话返回last
}

//顺序读写迭代器
template <typename ForwardIterator, typename panduan>
ForwardIterator new_remove_if(ForwardIterator b, ForwardIterator e, panduan p)
{
    ForwardIterator fail = b;
    for (; b != e; ++b)
    {
        if (!p(*b))
            *fail++ = *b; //使谓词为假的元素被放入开头
    }
    return fail; //返回第一个满足p元素所在的迭代器
}

int main()
{
    //transform，partition
    vector<int> vectint;
    list<int> listint;
    int chuan1, chuan2;
    
    cout << "请输入原串：" << endl;
    while (cin >> chuan1)
    {
        vectint.push_back(chuan1);
    }
    //cin.clear(); //清空输入流
    cout << "请输入要与原串匹配的串：" << endl;
    while (cin >> chuan2)
    {
        listint.push_back(chuan2);
    }
    typedef vector<int>::iterator iter1;
    typedef list<int>::iterator iter2;
    iter1 b = vectint.begin(), e = vectint.end(), last;
    iter2 b2 = listint.begin(), e2 = listint.end();
    
    //search函数
    last = new_search(b, e, b2, e2);
    cout << "库函数输出结果：" << *search(b, e, b2, e2) << endl; // 通过比较库函数与泛型函数输出结果判断是否正确
    cout << *last << endl;
    
    //find_if函数
    iter1 jieguo1;
    jieguo1 = new_find_if(b, e, p);
    cout << "原串中含7的话输出7，否则输出原串最后一位数，那么结果为：" << endl;
    cout << "库函数find_if输出结果：" << *(find_if(b, e, p) - 1) << endl;
    cout << "模板函数find_if输出结果：" << *jieguo1 << endl;
    
    //copy_if函数
    vector<int> vectint3(vectint.size());
    iter1 d = vectint3.begin();
    new_copy_if(b, e, d, p);
    cout << "将原串中所有为7的数字复制到新的容器中：" << endl;
    for (int n : vectint3)
        if (n != 0)
            cout << n << endl;
    
    //transform函数
    vector<int> vectint5(vectint.size());
    iter1 d5 = vectint5.begin();
    new_transform(b, e, d5, add6);
    // transform(b, e, d5, add6);
    cout << endl
    << "将原串中的数字+6：" << endl;
    for (int t : vectint5)
        cout << t << " ";
    
    //partition函数
    iter1 jieguo6, jieguo7;
    jieguo6 = new_partition(b, e, p);
    jieguo7 = partition(b, e, p);
    cout << endl;
    cout << "模板partition函数输出结果： " << *jieguo6 << endl;
    cout << "系统库partition函数输出结果：" << *jieguo7; // 调用系统库函数partition 看结果与自定义函数是否相同
    
    //remove_if函数
    iter1 jieguo4;
    jieguo4 = new_remove_if(b, e, p);
    cout << endl
    << "将原串中不为7的数字复制到新的容器中：" << endl;
    iter1 t = b;
    
    while (t != jieguo4)
        cout << *t++ << " ";
    cout << endl;
    
    return 0;
}
