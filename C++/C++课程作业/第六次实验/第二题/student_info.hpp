//
//  student_info.hpp
//  two6
//
//  Created by Worlder on 2018/12/31.
//  Copyright © 2018 Worlder. All rights reserved.
//

#ifndef student_info_hpp
#define student_info_hpp

#ifndef STUDENT_INFO
#define STUDENT_INFO

#include <fstream>
#include <string>
#include <vector>
using namespace std;

class stugrade
{
public:
    stugrade();
    stugrade(fstream &); //利用读入的信息初始化数据成员
    fstream &read(fstream &);
    
    void grade(); //求得学生平均成绩
    
    string name() const { return m_name; }                   //用于用户访问学生姓名
    double averagegrade() const { return m_averagegrade; } //用于用户访问学生最终成绩
    
private:
    double m_midgrade, m_finalgrade, m_averagegrade;
    string m_name;
};
bool compare(const stugrade &x, const stugrade &y);
bool if_pass(const stugrade &x);
#endif

#endif /* student_info_hpp */
