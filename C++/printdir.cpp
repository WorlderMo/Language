#include <unistd.h>
#include <stdio.h>
#include <dirent.h>
#include <string.h>
#include <sys/stat.h>
#include <stdlib.h>
#include "iostream"
#include <iomanip>
#include "vector"
#include "algorithm"
#include "regex"
using namespace std;

#define SORTBYNAME 1
#define SORTBYSIZE 2
#define SORTBYTIME 3

class File
{
  public:
    // File(arguments);
    // unsigned char d_type;
    string d_name;
    off_t st_size;
    time_t st_mtime;
    mode_t st_mode;

    char getFiletype()
    {
        return st_mode;
    }
    string getFilename()
    {
        return d_name;
    }
    off_t getFilesize()
    {
        return st_size;
    }
    time_t getFilectime()
    {
        return st_mtime;
    }
    bool isMatch(string grep)
    {
        regex re(grep);
        return regex_search(d_name, re);
    }
};

class IDSortStrategy
{
  public:
    virtual void sortFile(vector<File> &fileList) = 0;
};

static bool namecompare(const File &a, const File &b)
{
    return a.d_name < b.d_name;
}

class SortByFilename : public IDSortStrategy
{
  public:
    void sortFile(vector<File> &fileList)
    {
        /*
        根据文件名进行排序
        */
        sort(fileList.begin(), fileList.end(), namecompare);
    }
};

static bool sizecompare(const File &a, const File &b)
{
    return a.st_size < b.st_size;
}

class SortByFilesize : public IDSortStrategy
{
  public:
    void sortFile(vector<File> &fileList)
    {
        /*
        根据文件大小进行排序
        */
        sort(fileList.begin(), fileList.end(), sizecompare);
    }
};

static bool ctimecompare(const File &a, const File &b)
{
    return a.st_mtime < b.st_mtime;
}

class SortByFilectime : public IDSortStrategy
{
  public:
    void sortFile(vector<File> &fileList)
    {
        /*
        根据文件修改时间进行排序
        */
        sort(fileList.begin(), fileList.end(), ctimecompare);
    }
};

class SortFactory
{
  public:
    IDSortStrategy *ids;
    SortFactory(int sortby)
    {
        switch (sortby)
        {
        case SORTBYNAME:
            ids = new SortByFilename();
            break;
        case SORTBYSIZE:
            ids = new SortByFilesize();
            break;
        case SORTBYTIME:
            ids = new SortByFilectime();
            break;
        default:
            break;
        }
    }
};

vector<File> fileList;

void printdir(char *dir, int depth, string grep)
{
    /*
    打印目录dir下所有文件及目录：
    opendir(dir)打开目录，返回指向DIR结构体的指针dp
    readdir(dp)读取dir下所有文件(包括目录), 返回目录下所有文件的dirent结构体指针entry
    遍历entry:调用stat(entry->name, &statbuf)获取每个文件的详细信息存放在statbuf中
    */

    DIR *dp;
    struct dirent *entry;
    struct stat statbuf;

    if (NULL == (dp = opendir(dir)))
    {
        fprintf(stderr, "Can't open directory %s\n", dir);
        return;
    }

    chdir(dir);

    // 遍历dp结点
    while ((entry = readdir(dp)) != NULL)
    {
        // 获取每个结点信息, 放入到starbuf中
        stat(entry->d_name, &statbuf);

        if (S_ISDIR(statbuf.st_mode))
        {
            if (strcmp(entry->d_name, ".") == 0 || strcmp(entry->d_name, "..") == 0)
                continue;
            // printf("%*s%s/\n", depth, "", entry->d_name);
            // File file;
            // file.d_name = entry->d_name;
            // fileList.push_back(file);
            printdir(entry->d_name, depth + 4, grep);
        }
        else
        {
            // printf("%*s%s\n", depth, "", entry->d_name);
            File file;
            file.d_name = entry->d_name;
            if (file.isMatch(grep))
            {
                file.st_mode = statbuf.st_mode;
                file.st_size = statbuf.st_size;
                file.st_mtime = statbuf.st_mtime;
                fileList.push_back(file);
            }
        }
    }

    chdir("..");
    closedir(dp);
}

int main(int argc, char *argv[])
{
    char *topdir = (char *)malloc(256);
    if (argc >= 2)
        topdir = argv[1];
    char *grep = (char *)malloc(256);
    int sortby;
    while (1)
    {
        printf("请输入要扫描的目录：\n");
        gets(topdir);
        printf("请输入要搜索的文件关键字：\n");
        gets(grep);
        printf("请输入排序规则(1.文件名 2.文件大小 3.文件修改时间)：\n");
        scanf("%d", &sortby);
        printf("搜索目录 %s结果如下:\n", topdir);
        printdir(topdir, 0, grep);
        vector<File>::iterator iter;
        SortFactory *sortFactory = new SortFactory(sortby);
        sortFactory->ids->sortFile(fileList);
        printf("%-45s%-20s%-20s%-20s\n", "文件名", "文件大小(B)", "文件修改时间", "文件类型");
        for (iter = fileList.begin(); iter != fileList.end(); iter++)
        {
            cout.flags(ios::left);
            cout << setw(45) << (*iter).d_name << setw(20) << (*iter).st_size << setw(20) << (*iter).st_mtime << setw(20) << (*iter).st_mode << endl;
        }
        // 吸收字符输入
        getchar();
        fileList.clear();
    }
    exit(0);
}
