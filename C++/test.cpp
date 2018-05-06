/*******************************************************
@Date    : 2018-05-06 10:52:53
@Author  : mohailang (1198534595@qq.com)
*******************************************************/
#include <stdio.h>
#include <string.h>
int main(int argc, char const *argv[])
{
    char a[12] = "111";
    char b[21] = "22ssss";
    strcpy(a, b);
    printf("%s", a);

    return 0;
}
