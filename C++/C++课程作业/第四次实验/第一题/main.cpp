#include <vector>
#include <iostream>

#include "analysis.h"
#include "Student_info.h"

using namespace std;

int main()
{

	// students who did and didn't do all their homework
	vector<Student_info> did_girl, did_boy, didnt_boy, didnt_girl;

	// read the student records and partition them
	Student_info student;
	while (read(cin, student))
	{
		if (did_all_hw(student) && (student.gender == "girl"))
			did_girl.push_back(student);
		else if (did_all_hw(student) && (student.gender == "boy"))
			did_boy.push_back(student);
		else if ((!did_all_hw(student)) && (student.gender == "girl"))
			didnt_girl.push_back(student);
		else if ((!did_all_hw(student)) && (student.gender == "boy"))
			didnt_boy.push_back(student);
	}

	// verify that the analyses will show us something
	if (did_girl.empty())
	{
		cout << "No girl did all the homework!" << endl;
		return 1;
	}
	if (did_boy.empty())
	{
		cout << "No boy did all the homework!" << endl;
		return 1;
	}
	if (didnt_girl.empty())
	{
		cout << "Every girl did all the homework!" << endl;
		return 1;
	}
	if (didnt_boy.empty())
	{
		cout << "Every boy did all the homework!" << endl;
		return 1;
	}
	write_analysis(cout, "median", median_analysis, did_girl, did_boy, didnt_girl, didnt_boy);
	write_analysis(cout, "average", average_analysis, did_girl, did_boy, didnt_girl, didnt_boy);
	write_analysis(cout, "median of homework turned in",
				   optimistic_median_analysis, did_girl, did_boy, didnt_girl, didnt_boy);

	return 0;
}
