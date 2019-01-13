#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

int main()
{
  vector<int> u(10, 100);
  vector<int> v(u.size());
  copy(u.begin(), u.end(), v.begin());
  for (vector<int>::iterator it = v.begin(); it != v.end(); it++)
  {
    cout << (*it) << endl;
  }
  return 0;
}
