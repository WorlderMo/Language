//
//  main.cpp
//  five6
//
//  Created by Worlder on 2018/12/31.
//  Copyright © 2018 Worlder. All rights reserved.
//

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iterator>
#include "Student_info.hpp"
#include "median.hpp"
#include "grade.hpp"
using namespace std;

int creat = 0;
int copyy = 0;
int assignment = 0;
int destory = 0;

int main()
{
    cout << "请输入学生姓名和成绩：" << endl;
    vector<Student_info> students;
    Student_info record;
    string::size_type maxlen = 0;
    // 读入并存储学生信息
    while (record.read(cin))
    {                                                // 存储最长的学生姓名长度
        maxlen = max(maxlen, record.name().size()); // 将单个学生信息存vector中
        students.push_back(record);
    }
    
    //第一种方法
//     vector<Student_info> fail;
//     remove_copy_if(students.begin(), students.end(),
//     back_inserter(fail), pgrade);
//     students.erase(remove_if(students.begin(), students.end(),
//     fgrade), students.end());
    
    //第二种方法：
    vector<Student_info>::iterator iter =
    stable_partition(students.begin(), students.end(), pgrade);
    vector<Student_info> fail(iter, students.end());
    students.erase(iter, students.end());
    
    //将通过的同学显示出来
    cout << "通过的学生：" << endl;
    for (vector<Student_info>::size_type i = 0;
         i != students.size(); ++i)
    {
        cout << students[i].name() // 调用类的成员函数name以返回类的数据成员
        << string(maxlen + 1 - students[i].name().size(), ' ');
        try
        {
            double final_grade = students[i].grade();
            cout << final_grade << "\t" << endl;
        }
        catch (domain_error e)
        {
            cout << e.what() << endl;
        }
    }
    //将未通过的同学显示出来
    cout << "未通过的学生：" << endl;
    for (Student_info &j : fail)
    {
        cout << j.name() // 调用类的成员函数name以返回类的数据成员
        << string(maxlen + 1 - j.name().size(), ' ');
        try
        {
            double final_grade = j.grade();
            cout << final_grade << "\t" << endl;
        }
        catch (domain_error e)
        {
            cout << e.what() << endl;
        }
    }
    
    cout << "被创建的次数：" << creat << endl;
    cout << "被复制的次数：" << copyy << endl;
    cout << "被赋值的次数：" << assignment << endl;
    cout << "被销毁的次数：" << destory << endl;
    return 0;
}

