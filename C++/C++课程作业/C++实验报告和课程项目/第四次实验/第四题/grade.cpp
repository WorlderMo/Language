#include <stdexcept>
#include <vector>
#include <string>
#include "grade.h"
#include "median.h"
#include "Student_info.h"

using namespace std;

// compute a student's overall grade from midterm and final exam grades and homework grade
double grade(double midterm, double final, double homework)
{
	return 0.2 * midterm + 0.4 * final + 0.4 * homework;
}

// compute a student's overall grade from midterm and final exam grades
// and vector of homework grades.
// this function does not copy its argument, because `median' does so for us.
double grade(double midterm, double final, const vector<double> &hw)
{
	if (hw.size() == 0)
		throw domain_error("student has done no homework");
	return grade(midterm, final, median(hw));
}

double grade(const Student_info &s)
{
	return grade(s.midterm, s.final, s.homework);
}
string get_grade(double grade)
{
	if (grade >= 90.0)
		return "A";
	if (grade >= 80.0 && grade < 90.0)
		return "B";
	if (grade >= 70.0 && grade < 80.0)
		return "C";
	if (grade >= 60.0 && grade < 70.0)
		return "D";

	return "F";
}
 
