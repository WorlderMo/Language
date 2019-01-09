//
//  main.cpp
//  two6
//
//  Created by Worlder on 2018/12/31.
//  Copyright © 2018 Worlder. All rights reserved.
//

#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iterator>
#include "student_info.hpp"

using namespace std;

int main(int argc, char *argv[])
{
    fstream start;
    ofstream nonseparate, separate;
    start.open(argv[1]); //打开用于读入信息的文件
    vector<stugrade> students;
    stugrade onestudent;
    
    while (onestudent.read(start))
    { //将学生信息读入向量中
        students.push_back(onestudent);
    }
    
    nonseparate.open(argv[2]); //打开用于存储输出信息的文件
    sort(students.begin(), students.end(), compare);
    vector<stugrade>::iterator it = students.begin();
    for (; it != students.end(); ++it)
    {
        nonseparate << (*it).name() << "\t";
        if (if_pass(*it))
            nonseparate << "F" << endl; //若成绩未及格，函数if_pass返回值为1
        else
            nonseparate << "P" << endl;
    } //将全部学生按字母排序输出
    
    separate.open(argv[3]); //打开用于存储输出信息的文件
    auto it2 = remove_if(students.begin(), students.end(), if_pass);
    auto it3 = students.begin();
    
    separate << "PASS：" << endl;
    for (; it3 != it2; ++it3)
    {
        separate << (*it3).name() << endl;
    }
    separate << "FAIL：" << endl;
    for (; it2 != students.end(); ++it2)
    {
        separate << (*it2).name() << endl;
    }
    
    return 0;
}

