//
//  str.h
//  three7
//
//  Created by Worlder on 2019/1/1.
//  Copyright © 2019 Worlder. All rights reserved.
//

#ifndef str_h
#define str_h

#include <cctype>
#include <iostream>
#include "Vec.h"

class str
{
    
    friend std::istream &operator>>(std::istream &, str &);
    
public:
    typedef Vec<char>::size_type size_type;
    
    //默认构造函数
    str() {}
    
    //生成一个str对象，包含n个c
    str(size_type n, char c) : data(n, c) {}
    
    //生成一个str对象并使用一个空字符结尾的字符数组来初始化
    str(const char *cp)
    {
        std::copy(cp, cp + std::strlen(cp), std::back_inserter(data));
    }
    
    //生成一个str对象并使用迭代器b和e之间的内容对它进行初始化
    template <class In>
    str(In b, In e)
    {
        std::copy(b, e, std::back_inserter(data));
    }
    
    //重载索引运算符
    char &operator[](size_type i) { return data[i]; }
    const char &operator[](size_type i) const { return data[i]; }
    //返回长度
    size_type size() const { return data.size(); }
    //+=操作符
    str &operator+=(const str &s)
    {
        std::copy(s.data.begin(), s.data.end(), std::back_inserter(data));
        return *this;
    }
    
private:
    Vec<char> data;
};

str operator+(const str &, const str &);
std::ostream &operator<<(std::ostream &, const str &);

//输入输出
std::istream &operator>>(std::istream &is, str &s)
{
    //清空s中存在的值
    s.data.clear(); //private;
    //按序读字符并忽略前面的空格字符
    char c;
    while (is.get(c) && isspace(c))
        ;
    if (is)
    {
        do
            s.data.push_back(c);
        while (is.get(c) && !isspace(c));
        if (is)
            is.unget();
    }
    return is;
}

std::ostream &operator<<(std::ostream &os, const str &s)
{
    for (str::size_type i = 0; i != s.size(); ++i)
        os << s[i];
    return os;
}

str operator+(const str &s, const str &t)
{
    str r = s;
    r += t;
    return r;
}
bool operator>(const str &s, const str &t)
{
    int i = s.size(), j = t.size(), min = 0, temp = 0;
    
    if (i > j)
        min = j;
    else
        min = i;
    
    for (; temp != min; ++temp)
    {
        if (s[temp] != t[temp])
            break;
    }
    if (temp < min)
    {
        if (s[temp] > t[temp])
            return true;
        else
            return false;
    }
    else
    {
        if (i > j)
            return true;
        else
            return false; //i与j相等或者i是j的字串
    }
}
bool operator<(const str &s, const str &t)
{
    int i = s.size(), j = t.size(), min = 0, temp = 0;
    
    if (i > j)
        min = j;
    else
        min = i;
    
    for (; temp != min; ++temp)
    {
        if (s[temp] != t[temp])
            break;
    }
    if (temp < min)
    {
        if (s[temp] < t[temp])
            return true;
        else
            return false;
    }
    else
    {
        if (i < j)
            return true;
        else
            return false;
    }
}
bool operator==(const str &s, const str &t)
{
    int i = s.size();
    if (i == t.size())
    {
        int j = 0;
        for (; j != i; ++j)
        {
            if (s[j] != t[j])
                break;
        }
        if (j == i)
            return true;
        else
            return false;
    }
    else
        return false;
}

bool operator!=(const str &s, const str &t)
{
    int i = s.size();
    int j = 0;
    for (; j != i; ++j)
    {
        if (s[j] != t[j])
            break;
    }
    if (j < i)
        return true;
    else if (i == t.size())
        return false;
    else
        return true;
}

#endif /* str_h */
