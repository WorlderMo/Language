//
//  student_info.cpp
//  two6
//
//  Created by Worlder on 2018/12/31.
//  Copyright © 2018 Worlder. All rights reserved.
//

#include "student_info.hpp"
#include <fstream>
#include <string>
#include <vector>

//初始化期中期末以及最终成绩  初始化列表
stugrade::stugrade() : m_midgrade(0), m_finalgrade(0), m_averagegrade(0) {}

stugrade::stugrade(fstream &in) { read(in); }

fstream &stugrade::read(fstream &in)
{
    //将文件中信息读入
    in >> m_name >> m_midgrade >> m_finalgrade;
    //求得学生的最终成绩
    grade();
    return in;
}

void stugrade::grade()
{
    m_averagegrade = (m_midgrade + m_finalgrade) / 2;
    return;
}

bool compare(const stugrade &x, const stugrade &y)
{
    return x.name() < y.name();
}

bool if_pass(const stugrade &x)
{
    return x.averagegrade() < 60;
}
