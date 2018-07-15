/**
  *@Date    : 2018-07-15 19:37:41
  *@Author  : mohailang (1198534595@qq.com)
  **/
#include <sys/types.h>
#include <unistd.h>

int main(int argc, char const *argv[])
{
    int a = 3, b;
    if (fork() == 0)
    {
        a++;
        printf("a=%d\n", a);
    }

    a = a - 1;
    printf("a=%d\n", a);

    return 0;
}
