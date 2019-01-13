#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

int main(int argc, char const *argv[])
{
     vector<string> words;
     vector<string> result;
     string str;
     string test_str;
     cout << "请输入字符串个数：" << endl;
     int count;
     cin >> count;
     cout << "请输入字符串：" << endl;
     for (int i = 0; i < count; i++)
     {
          cin >> str;
          words.push_back(str);
     }
     cout << "请输入前缀：" << endl;
     cin >> test_str;
     int a = test_str.length();
     int len = words.size();
     for (int i = 0; i < len; i++)
     {
          string sub_str = words[i].substr(0, a);
          if (sub_str == test_str)
          {
               result.push_back(words[i]);
          }
     }
     for (vector<string>::iterator it = result.begin(); it != result.end(); it++)
          cout << *it << " ";
     return 0;
}
