//
//  grade.cpp
//  five6
//
//  Created by Worlder on 2018/12/31.
//  Copyright © 2018 Worlder. All rights reserved.
//

#include <vector>
#include <stdexcept>
#include <string>
#include "grade.hpp"
#include "median.hpp"
#include "Student_info.hpp"

using namespace std;

// compute a student's overall grade from midterm and final exam grades and homework grade
double grade(double midterm, double final, double homework)
{
    double finalgrade = 0.2 * midterm + 0.4 * final + 0.4 * homework;
    return finalgrade;
}

double grade(double midterm, double final, const vector<double>& hw)
{
    if (hw.size() == 0)
        throw domain_error("student has done no homework");
    return grade(midterm, final, median(hw));
}
bool fgrade( Student_info& s)
{
    return s.grade() < 60;
}

bool pgrade( Student_info& s)
{
    return !fgrade(s);
}
