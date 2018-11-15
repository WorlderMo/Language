#include <algorithm>
#include <iterator>
#include <vector>
#include <iostream>

using namespace std;

int main()
{
  vector<int> u(10, 100);
  vector<int> v;
  copy(u.begin(), u.end(), back_inserter(v));
  //  copy(u.begin(), u.end(), inserter(v, v.begin()));
  for (vector<int>::iterator it = v.begin(); it != v.end(); it++)
  {
    cout << (*it) << endl;
  }
  return 0;
}
