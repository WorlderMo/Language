//
//  grade.hpp
//  five6
//
//  Created by Worlder on 2018/12/31.
//  Copyright © 2018 Worlder. All rights reserved.
//

#ifndef grade_hpp
#define grade_hpp

#include <stdio.h>
#include <string>
#include <vector>
#include"Student_info.hpp"
using namespace std;

double grade(double, double, const vector<double>&);
bool fgrade( Student_info& s);
bool pgrade( Student_info& s);

#endif /* grade_hpp */
