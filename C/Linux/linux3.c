/**
 *  *@Date    : 2018-06-15 16:19:54
  *@Author  : mohailang (1198534595@qq.com)
  **/

#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>

int main(int argc, char const *argv[])
{
    int a, fd, file;
    char b[32];
    char c[5] = "over";
    fd = fork();
    file = open("test.txt", O_RDWR | O_APPEND);

    if (fd < 0)
    {
        printf("创建子进程失败");
    }
    else if (fd == 0)
    {
        //第一次读且读到文件末尾
        read(file, b, sizeof(b));
        sleep(3);
        a = read(file, b, sizeof(b));
        printf("a=%d\n", a);
    }
    else
    {
        //让子进程先执行
        sleep(1);
        //在文件末尾追加字符
        write(file, c, sizeof(c));
        wait(NULL);
        close(file);
    }
    return 0;
}
