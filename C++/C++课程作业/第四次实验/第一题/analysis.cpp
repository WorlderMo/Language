#include <algorithm>
#include <iostream>
#include <iterator>
#include <numeric>
#include <stdexcept>
#include <vector>

#include "analysis.h"
#include "Student_info.h"
#include "grade.h"
#include "median.h"
using namespace std;
bool did_all_hw(const Student_info &s)
{
	return ((find(s.homework.begin(), s.homework.end(), 0)) == s.homework.end());
}

double grade_aux(const Student_info &s)
{
	try
	{
		return grade(s);
	}
	catch (domain_error)
	{
		return grade(s.midterm, s.final, 0);
	}
}

// this version works fine
double median_analysis(const vector<Student_info> &students)
{
	vector<double> grades;

	transform(students.begin(), students.end(),
			  back_inserter(grades), grade_aux);
	return median(grades);
}
void write_analysis(std::ostream &out, const std::string &name,
					double analysis(const std::vector<Student_info> &),
					const std::vector<Student_info> &did_girl, const std::vector<Student_info> &did_boy,
					const std::vector<Student_info> &didnt_girl, const std::vector<Student_info> &didnt_boy)
{
	out << name << ": median(did_girl) = " << analysis(did_girl) << "  median(did_boy) = " << analysis(did_boy) << ", median(didnt_girl) = " << analysis(didnt_girl) << ", median(didnt_boy) = " << analysis(didnt_boy) << endl;
}

double average(const vector<double> &v)
{
	return accumulate(v.begin(), v.end(), 0.0) / v.size();
}

double average_grade(const Student_info &s)
{
	return grade(s.midterm, s.final, average(s.homework));
}

double average_analysis(const vector<Student_info> &students)
{
	vector<double> grades;

	transform(students.begin(), students.end(),
			  back_inserter(grades), average_grade);
	return median(grades);
}

// median of the nonzero elements of `s.homework', or `0' if no such elements exist
double optimistic_median(const Student_info &s)
{
	vector<double> nonzero;
	remove_copy(s.homework.begin(), s.homework.end(),
				back_inserter(nonzero), 0);

	if (nonzero.empty())
		return grade(s.midterm, s.final, 0);
	else
		return grade(s.midterm, s.final, median(nonzero));
}

double optimistic_median_analysis(const vector<Student_info> &students)
{
	vector<double> grades;

	transform(students.begin(), students.end(),
			  back_inserter(grades), optimistic_median);
	return median(grades);
}
#
