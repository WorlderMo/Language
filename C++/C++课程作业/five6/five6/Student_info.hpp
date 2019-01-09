//
//  Student_info.hpp
//  five6
//
//  Created by Worlder on 2018/12/31.
//  Copyright © 2018 Worlder. All rights reserved.
//

#ifndef Student_info_hpp
#define Student_info_hpp

#include <stdio.h>
#include <string>
#include <vector>
#include <iostream>
using namespace std;

extern int creat;      //被创建的次数
extern int copyy;      //被复制的次数
extern int assignment; //被赋值的次数
extern int destory;    //被销毁的次数

class Student_info
{
public:
    Student_info()
    { // 重新定义无任何参数的构造函数
        ++creat;
        midterm = 0;
        final = 0;
    };
    
    Student_info(std::istream &is) { read(is); }; // 参数为输入流的构造函数
    
    Student_info(const Student_info &v) //重新定义复制构造函数
    {
        ++copyy;
        this->n = v.n;
        this->midterm = v.midterm;
        this->final = v.final;
        this->homework = v.homework;
    };
    
    Student_info &operator=(const Student_info &rhs) //重载赋值操作符
    {
        if (&rhs != this)
        {
            ++assignment;
            homework.clear();
            this->n = rhs.n;
            this->midterm = rhs.midterm;
            this->final = rhs.final;
            this->homework = rhs.homework;
        }
        return *this;
    }
    
    ~Student_info()
    { //重新定义析构函数
        ++destory;
        homework.clear();
    }
    string name() const { return n; }
    bool valid() const { return !homework.empty(); }
    istream &read(istream &);
    double grade();
    
private:
    string n; //学生姓名
    double midterm, final;
    vector<double> homework;
};

bool compare(const Student_info &, const Student_info &);
#endif /* Student_info_hpp */
