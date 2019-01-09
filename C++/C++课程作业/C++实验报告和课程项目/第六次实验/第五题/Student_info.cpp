//
//  Student_info.cpp
//  five6
//
//  Created by Worlder on 2018/12/31.
//  Copyright © 2018 Worlder. All rights reserved.
//

#include <iostream>
#include <vector>
#include "grade.hpp"
#include "Student_info.hpp"
#include <string>
using namespace std;

double Student_info::grade() //不改变对象状态
{
    return ::grade(midterm, final, homework); //全局函数
}

bool compare(const Student_info &x, const Student_info &y)
{
    return x.name() < y.name();
}

// read homework grades from an input stream into a `vector<double>'
istream &read_hw(istream &in, vector<double> &hw)
{
    if (in)
    {
        // get rid of previous contents
        hw.clear();
        
        // read homework grades
        double x;
        while (in >> x)
            hw.push_back(x);
        
        // clear the stream so that input will work for the next student
        in.clear();
    }
    return in;
}

istream &Student_info::read(istream &in)
{
    in >> n >> midterm >> final;
    read_hw(in, homework);
    return in;
}
