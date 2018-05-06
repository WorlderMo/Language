/*******************************************************
@Date    : 2018-05-06 10:52:53
@Author  : mohailang (1198534595@qq.com)
*******************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <dirent.h>
#include <string.h>
#include <vector>
#include <iostream>

using namespace std;
vector<int> a;
vector<int> b;
int main(void)
{
    a.push_back(1);
    a.push_back(2);
    a.push_back(3);

    b.push_back(4);
    b.push_back(5);
    b.push_back(6);

    b.insert(b.begin(), a.begin(), a.end());

    for (int i = 0; i < b.size(); i++)
        cout << b[i];
    return 0;
}
