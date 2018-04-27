#include <algorithm>
#include <iomanip>
#include <ios>
#include <iostream>
#include <string>
#include <vector>

using std::cin; using std::sort;
using std::cout; using std::streamsize;
using std::endl; using std::string;
using std::setprecision; using std::vector;

int main(int argc, char const *argv[])
{
    //请求输入学生的姓名
    cout << "请输入你的名字：";
    string name;
    cin >> name;
    cout << "Hello, " << name << "!" << endl;

    //请求输入并读入期中和期末成绩
    cout << "请输入你的期中和期末成绩：";
    double midterm, finalterm;
    cin >> midterm >> finalterm;

    //请求输入家庭作业成绩
    cout << "请输入你的家庭作业成绩: ";
    vector<double> homework;
    double x;
    //不变式：homework包含所有的家庭作业成绩
    while (cin >> x)
    {
        homework.push_back(x);
    }
    //检查homework是否为空
    typedef vector<double>::size_type vec_sz;
    vec_sz size = homework.size();
    if (size == 0)
    {
        cout << "请输入你的家庭作业成绩，再次尝试" << endl;
        return 1;
    }

    //对成绩进行排序
    sort(homework.begin(), homework.end());

    //计算家庭作业的中值
    vec_sz mid = size/2;
    double median;
    median = size % 2 == 0 ? (homework[mid] + homework[mid-1])/2 : homework[mid];

    //计算并输出总成绩
    streamsize prec = cout.precision();
    cout << "你的最终成绩为：" << setprecision(3)
    << 0.2 * midterm + 0.4 * finalterm + 0.4 * median
    << setprecision(prec) << endl;
    return 0;
}
