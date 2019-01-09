#include <algorithm>
#include <iomanip>
#include <ios>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
#include <map>
#include "grade.h"
#include "Student_info.h"
using namespace std;

int main()
{
	vector<Student_info> students;
	Student_info record;
	string::size_type maxlen = 0;

	map<string, int> level;

	while (read(cin, record))
	{
		maxlen = max(maxlen, record.name.size());
		students.push_back(record);
	}

	sort(students.begin(), students.end(), compare);

	for (vector<Student_info>::size_type i = 0;
		 i != students.size(); ++i)
	{

		try
		{
			double final_grade = grade(students[i]);
			level[get_grade(final_grade)]++;
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

	map<string, int>::iterator it;
	for (it = level.begin(); it != level.end(); ++it)
	{
		cout << it->first << ": " << it->second << endl;
	}
	return 0;
}
  
