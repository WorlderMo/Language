#include <algorithm>
#include <iomanip>
#include <iostream>
#include <stdexcept>
#include <map>
#include <string>
#include <vector>

using namespace std;

struct Student_info {
  string name;
  double midterm, final;
  vector<double> homework;
};


double median(vector<double> vec) {
  typedef vector<double>::size_type vec_sz;

  vec_sz size = vec.size();
  if (size == 0)
    throw domain_error("错误");

  sort(vec.begin(), vec.end());

  vec_sz mid = size/2;

  return size % 2 == 0 ? (vec[mid] + vec[mid-1]) / 2 : vec[mid];
}

double grade(double midterm, double final, double homework) {
  return 0.2 * midterm + 0.4 * final + 0.4 * homework;
}


double grade(double midterm, double final, const vector<double>& hw) {
  if (hw.size() == 0)
    throw domain_error("学生没有写作业");

  return grade(midterm, final, median(hw));
}

double grade(const Student_info& s) {
  return grade(s.midterm, s.final, s.homework);
}

istream& read_hw(istream& in, vector<double>& hw) {
  if (in) {
    hw.clear();

    double x;
    while (in >> x)
      hw.push_back(x);

    in.clear();
  }

  return in;
}

istream& read(istream& is, Student_info& s) {
  is >> s.name >> s.midterm >> s.final;

  read_hw(is, s.homework);

  return is;
}

bool compare(const Student_info& x, const Student_info& y) {
  return x.name < y.name;
}

string get_letter_grade(double grade) {
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

int main() {
  vector<Student_info> students;
  Student_info record;
  string::size_type maxlen = 0;
  map<string, int> letter_grade_counts;

  while (read(cin, record)) {
    maxlen = max(maxlen, record.name.size());
    students.push_back(record);
  }

  sort(students.begin(), students.end(), compare);

  for (vector<Student_info>::size_type i = 0;
       i != students.size(); ++i) {
    try {
      double final_grade = grade(students[i]);
      letter_grade_counts[get_letter_grade(final_grade)]++;
    } catch (domain_error e) {
      cout << e.what();
    }
  }

  for (map<string, int>::const_iterator i = letter_grade_counts.begin();
       i != letter_grade_counts.end(); ++i)
    cout << i->first << ": " << i->second << endl;

  return 0;
}
