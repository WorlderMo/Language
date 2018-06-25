/**
 *@Date    : 2018-06-20 21:14:15
 *@Author  : mohailang (1198534595@qq.com)
**/

#include <stdio.h>
#include <stdlib.h>

int i = 1; //计算申请空间的次数
void test()
{
    //一次申请1M空间便于计算
    char a[1048576];
    printf("第%d次申请 %ld字节空间 %p\n", i, sizeof(a), a);

    i++;
    test();
}

int main(int argc, char const *argv[])
{
    test();
    return 0;
}
