//
//  main.cpp
//  one6
//
//  Created by Worlder on 2018/12/31.
//  Copyright © 2018 Worlder. All rights reserved.
//

#include <algorithm>
#include <iomanip>
#include <ios>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

#include "Student_info.hpp"
#include "median.hpp"

int main()
{
    vector<Student_info> students;
    Student_info record;
    string::size_type maxlen = 0;
    // 读入并存储学生信息
    while (record.read(cin))
    {                                                // 存储最长的学生姓名长度
        maxlen = max(maxlen, record.name().size()); // 将单个学生信息存vector中
        students.push_back(record);
    }
    
    //按字母升序排列vector
    sort(students.begin(), students.end(), compare);
    // write the names and grades
    for (vector<Student_info>::size_type i = 0;
         i != students.size(); ++i)
    {
        cout << students[i].name() // 调用类的成员函数name以返回类的数据成员
        << string(maxlen + 1 - students[i].name().size(), ' ');
        try
        {
            double final_grade = students[i].grade(); // changed
            streamsize prec = cout.precision();
            cout << setiosflags(ios::fixed) << setprecision(2) << final_grade << "\t"
            << "转换后的成绩：" << students[i].alpgrade() << setprecision(prec) << endl;
        }
        catch (domain_error e)
        {
            cout << e.what() << endl;
        }
    }
    return 0;
}

