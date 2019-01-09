//
//  Student_info.hpp
//  one6
//
//  Created by Worlder on 2018/12/31.
//  Copyright © 2018 Worlder. All rights reserved.
//

#ifndef Student_info_hpp
#define Student_info_hpp

#include <string>
#include <vector>
class Student_info
{
public:
    Student_info();                  // 无任何参数的构造函数
    Student_info(std::istream &); // 参数为输入流的构造函数
    std::string name() const { return n; }
    bool valid() const { return !homework.empty(); }
    double alpgrade() const { return rank; } //返回学生字母成绩
    // as defined in 9.2.1/157, and changed to read into `n' instead of `name'
    std::istream &read(std::istream &);
    
    double grade(); // as defined in 9.2.1/158
private:
    std::string n; //学生姓名
    double midterm, final;
    double rank; //存储学生五分制成绩
    std::vector<double> homework;
};

bool compare(const Student_info &, const Student_info &);

#endif /* Student_info_hpp */
