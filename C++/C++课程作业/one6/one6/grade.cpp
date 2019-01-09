//
//  grade.cpp
//  one6
//
//  Created by Worlder on 2018/12/31.
//  Copyright © 2018 Worlder. All rights reserved.
//

#include <vector>
#include <stdexcept>
#include "grade.hpp"
#include "median.hpp"
#include <string>
using namespace std;

// compute a student's overall grade from midterm and final exam grades and homework grade
double grade(double midterm, double final, double homework, double &rank)
{
    double finalgrade = 0.2 * midterm + 0.4 * final + 0.4 * homework;
    if (finalgrade >= 90 && finalgrade <= 100)
        rank = 4 + (finalgrade - 90) / 10; //生成字母成绩
    else if (finalgrade >= 80 && finalgrade < 90)
        rank = 3 + (finalgrade - 80) / 10;
    else if (finalgrade >= 70 && finalgrade < 80)
        rank = 2 + (finalgrade - 70) / 10;
    else if (finalgrade >= 60 && finalgrade < 70)
        rank = 1 + (finalgrade - 60) / 10;
    else
        rank = 0;
    return finalgrade;
}

// compute a student's overall grade from midterm and final exam grades
// and vector of homework grades.
// this function does not copy its argument, because `median' does so for us.
double grade(double midterm, double final, const vector<double> &hw, double &rank)
{
    if (hw.size() == 0)
        throw domain_error("student has done no homework");
    return grade(midterm, final, median(hw), rank);
}
