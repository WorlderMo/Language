#include <algorithm>
#include <iomanip>
#include <ios>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
#include "grade.h"
#include "Student_info.h"

using std::cin;
using std::cout;
using std::domain_error;
using std::endl;
using std::max;
using std::setprecision;
using std::sort;
using std::streamsize;
using std::string;
using std::vector;

int main()
{
	vector<Student_info> students;
	Student_info record;
	string::size_type maxlen = 0; // the length of the longest name

	// read and store all the students' data.
	// Invariant:	`students' contains all the student records read so far
	//			`maxlen' contains the length of the longest name in `students'
	while (read(cin, record))
	{
		// find length of longest name
		maxlen = max(maxlen, record.name.size());
		students.push_back(record);
	}

	// alphabetize the student records
	sort(students.begin(), students.end(),
		 [](const Student_info &x, const Student_info &y) {
			 return (x.name < y.name);
		 });

	// write the names and grades
	for (Student_info &s : students)
	{

		// write the name, padded on the right to `maxlen' `+' `1' characters
		cout << s.name
			 << string(maxlen + 1 - s.name.size(), ' ');

		// compute and write the grade
		try
		{
			double final_grade = s.finalGrade;
			streamsize prec = cout.precision();
			cout << setprecision(3) << final_grade
				 << setprecision(prec);
		}
		catch (domain_error e)
		{
			cout << e.what();
		}
		cout << endl;
	}
	return 0;
}
