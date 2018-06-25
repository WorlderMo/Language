#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#define MAX_FILES 20480
int main(int argc, char const *argv[])
{
    int i;
    int fd;
    char a[8];
    int count = 3; //程序启动时打开了三个文件
    for (i = 3; i < MAX_FILES; i++)
    {
        char buf[24] = "f_";
        sprintf(a, "%d", i);
        strcat(buf, a); //将文件名追加到文件路径末
        printf("file_name:%s\n", buf);
        fd = open(buf, O_RDWR | O_CREAT, S_IRUSR);
        if (fd != -1)
        {
            //输出文件标识符
            count++;
            printf("==fd:%d==\n", fd);
            printf("Opened %d files\n", count);
        }
        else
        {
            //输出一共能打开的文件数
            printf("open error, can only open %d files\n", count);
            return 0;
        }
    }
    return 0;
}
