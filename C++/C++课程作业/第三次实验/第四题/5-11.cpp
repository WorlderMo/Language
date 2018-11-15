#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main()
{
    string word;
    string s = "dfhkltgjpqy";
    string::size_type n;
    int j, count, k;
    vector<string> non_;
    vector<string>::size_type max;
    cout << "请输入单词\n";
    while (cin >> word)
    {
        string::size_type i;
        count = 0;
        for (i = 0; i != word.size(); i++)
        {
            for (j = 0; j < 11; j++)
            {
                if (word[i] == s[j])
                    count++;
                continue;
            }
        }
        if (count == 0)
            non_.push_back(word);
    }
    max = non_[0].size();
    for (n = 1; n != non_.size(); n++)
    {
        if (non_[n].size() > max)
        {
            max = non_[n].size();
            k = n;
        }
    }
    cout << "最长无上行字母下行字母的字符串为:" << non_[k] << endl;
    return 0;
}
