/**
 *@Date    : 2018-06-21 21:46:59
 *@Author  : mohailang (1198534595@qq.com)
**/

#include <stdio.h>
#include <stdlib.h>

int i = 1; //记录申请空间的次数
void test()
{
    //一次申请1M空间便于计算
    char a[1048576] = {"1"};
    char *p = NULL;

    p = (char *)malloc(1048576);

    printf("第%d次申请 %ld 字节空间 %p --><-- %p\n", i, sizeof(a), a, p);

    i++;
    test();
}

int main(int argc, char const *argv[])
{
    test();
    return 0;
}
