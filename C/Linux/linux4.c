/**
 *  *@Date    : 2018-06-15 17:03:47
  *@Author  : mohailang (1198534595@qq.com)
  **/

#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
int main(int argc, char const *argv[])
{
    int a, f, fd;
    FILE *p = NULL;
    char b[32];
    char c[5] = "over";
    fd = fork();
    p = fopen("text.txt", "a+");
    if (fd < 0)
    {
        printf("fork error\n");
    }
    else if (fd == 0)
    {
        fread(b, sizeof(char), 32, p);
        sleep(3);
        a = fread(b, sizeof(char), 32, p);
        printf("a=%d\n", a);
    }
    else
    {
        sleep(1);
        fwrite(c, sizeof(char), 5, p);
        wait(NULL);
        fclose(p);
    }
    return 0;
}
