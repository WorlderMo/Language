// source file for `Student_info'-related functions
#include "pch.h"
#include "Student_info.h"
#include "grade.h"
#include<iostream>

using std::istream;  using std::vector; using std::cin;

istream& read(istream& is, Student_info& s)
{
	// read and store the student's name and midterm and final exam grades
	double midterm, final;
	is >> s.name >> midterm >>final;
	vector<double> homework;
	read_hw(is, homework);  // read and store all the student's homework grades
	if(is) s.finalGrade = grade(midterm, final, homework);
	return is;
}

// read homework grades from an input stream into a `vector<double>'
istream& read_hw(istream& in, vector<double>& hw)
{
	if (in) {
		// get rid of previous contents
		hw.clear();

		// read homework grades
		double x;
		while (in >> x) 
			hw.push_back(x);

		in.clear();
	}
	return in;
}