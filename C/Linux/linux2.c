/**
 *  *@Date    : 2018-06-15 12:19:29
  *@Author  : mohailang (1198534595@qq.com)
  **/

#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>

int main(int argc, char const *argv[])
{
    int fd, file;
    char a[16] = "我是子进程";
    char b[16] = "我是父进程";
    //创建子进程
    fd = fork();
    //打开文件如果不存在就先创建
    file = open("test.txt", O_RDWR | O_APPEND | O_CREAT, 777);
    if (fd < 0)
    {
        printf("创建子进程失败");
    }
    else if (fd == 0)
    {
        //子进程写文件
        write(file, a, sizeof(a));
    }
    else
    {
        //父进程写文件
        write(file, b, sizeof(b));
        //等待子进程结束
        wait(NULL);
        close(file);
    }
    return 0;
}
