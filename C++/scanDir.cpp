// @Date : 2018 - 04 - 19 22 : 24 : 43
// @Author : mohailang(1198534595 @qq.com)

#include <iostream>
#include <string>
#include <vector>
#include <sys/stat.h>
#include <regex.h>
#include <libgen.h>
#include <dirent.h>
#include <assert.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

using namespace std;
vector<string> file_vector;

//文件匹配
int macth_regex(const char *buffer, const char *pattern)
{
    regex_t reg;
    regmatch_t pm[1] = {0};
    int ret = 0;
    char errbuf[1024] = {0};
    ret = regcomp(&reg, pattern, REG_EXTENDED | REG_ICASE);
    if (ret != 0)
    {
        regerror(ret, &reg, errbuf, sizeof(errbuf));
        fprintf(stderr, "%s:regcom(%s)\n", errbuf, pattern);
        return -1;
    }
    if (regexec(&reg, buffer, 1, pm, 0) == 0)
    {
        regfree(&reg);
        return 0; //匹配成功
    }
    else
    {
        regfree(&reg);
        return -1;
    }
}

//递归扫描目录
int scanDir(char *path, char *pattern)
{
    int i, j;
    char file_path[512] = {0};
    char file[512] = {0};
    DIR *dir = NULL;
    struct dirent *ptr = NULL;
    struct stat buf;

    if ((dir = opendir(path)) == NULL)
    {
        perror("opendir failed!");
        return -1;
    }
    while ((ptr = readdir(dir)) != NULL)
    {
        if (ptr->d_name[0] != '.')
        {
            strcpy(file_path, path);
            if (path[strlen(path) - 1] != '/')
                strcat(file_path, "/");
            strcat(file_path, ptr->d_name); //构建完整的文件名
            assert(stat(file_path, &buf) != -1);
            if (S_ISREG(buf.st_mode))
            {
                for (i = 0; i < strlen(file_path); i++)
                {
                    if (file_path[i] == '/')
                    {
                        memset(file, 0, strlen(file));
                        j = 0;
                        continue;
                    }
                    file[j++] = file_path[i];
                }
                if (macth_regex(file, pattern) == 0)
                {
                    file_vector.push_back(file_path);
                }
            }
            else if (S_ISDIR(buf.st_mode))
            {
                scanDir(file_path, pattern);
            }
        }
    }
    return 0;
}

int main(int argc, char const *argv[])
{
    char path[512];
    char pattern[32];
    printf("请输入想要扫描的目录路径:\n");
    scanf("%s", path);
    printf("请输入想要扫描的文件关键字:\n");
    scanf("%s", pattern);
    printf("查找到以下相关文件:\n");
    scanDir(path, pattern);
    for (int i = 0; i < file_vector.size(); i++)
    {
        cout << file_vector[i] << endl;
    }
    return 0;
}
