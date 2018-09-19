/**
  *@Date    : 2018-07-15 19:37:41
  *@Author  : mohailang (1198534595@qq.com)
  **/
#include <sys/types.h>
#include <unistd.h>
# define DOUBLE(x) x+x
int main(int argc, char const *argv[])
{
    float i = 7*DOUBLE(2);
    printf('%f',i);
    return 0;
}
