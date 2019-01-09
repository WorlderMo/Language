#ifndef GUARD_grade_h
#define GUARD_grade_h


#include <vector>
#include <string>
#include "Student_info.h"
using namespace std;
double grade(double, double, double);
double grade(double, double, const std::vector<double>&);
double grade(const Student_info&);
string get_grade(double grade);
 
#endif
