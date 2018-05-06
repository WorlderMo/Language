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
void print_usage(void);

int main(int argc, char *argv[])
{
    DIR *dir = NULL;
    struct dirent *ptr = NULL;
    struct stat *buf;
    char path[512] = "/Users/worlder/Documents/Language/C++";
    dir = opendir(path);
    char a[12] = "AAAAAA";
    while ((ptr = readdir(dir)) != NULL)
    {
        printf("%s\n", ptr->d_name);
    }
    strcat(a, ptr->d_name);
    printf("%s", a);

    return 0;
}
