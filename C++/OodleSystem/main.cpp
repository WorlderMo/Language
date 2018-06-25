/**
 *@Date    : 2018-04-20 10:22:35
 *@Author  : mohailang (1198534595@qq.com)
**/

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
#include <fstream>
#include <iomanip>
#include <unistd.h>

using namespace std;

#define SORTBYFILENAME 1
#define SORTBYFILESIZE 2
#define SORTBYFILETIME 3

class FileInfo
{
  public:
    string fileName;
    off_t fileSize;
    string fileTime;

    string getFileName() const
    {
        return fileName;
    }

    bool operator==(const FileInfo &file)
    {
        if (file.fileName == fileName && file.fileSize == fileSize &&
            file.fileTime == fileTime)
        {
            return true;
        }
        return false;
    }
    bool operator!=(const FileInfo &file)
    {
        if (file.fileName == fileName && file.fileSize == fileSize &&
            file.fileTime == fileTime)
        {
            return false;
        }
        return true;
    }
};

vector<FileInfo> fileVector;

class SortStrategy
{
  public:
    virtual void sortFile(vector<FileInfo> &fileList) = 0;
};

//文件名比较
static bool fileNameCompare(const FileInfo &a, const FileInfo &b)
{
    return a.fileName < b.fileName;
}

class SortByFileName : public SortStrategy
{
  public:
    void sortFile(vector<FileInfo> &fileList)
    {
        //根据文件名排序
        sort(fileList.begin(), fileList.end(), fileNameCompare);
    }
};
//文件大小比较
static bool fileSizeCompare(const FileInfo &a, const FileInfo &b)
{
    return a.fileSize < b.fileSize;
}

class SortByFileSize : public SortStrategy
{
  public:
    void sortFile(vector<FileInfo> &fileList)
    {
        //根据文件大小进行排序
        sort(fileList.begin(), fileList.end(), fileSizeCompare);
    }
};

//文件时间比较
static bool fileTimeCompare(const FileInfo &a, const FileInfo &b)
{
    return a.fileTime < b.fileTime;
}

class SortByFileTime : public SortStrategy
{
  public:
    void sortFile(vector<FileInfo> &fileList)
    {
        //根据文件大小进行排序
        sort(fileList.begin(), fileList.end(), fileTimeCompare);
    }
};

//文件排序
class SortFactory
{
  public:
    SortStrategy *sortID;
    SortFactory(int sortBy)
    {
        switch (sortBy)
        {
        case SORTBYFILENAME:
            sortID = new SortByFileName();
            break;
        case SORTBYFILESIZE:
            sortID = new SortByFileSize();
            break;
        case SORTBYFILETIME:
            sortID = new SortByFileTime();
            break;
        default:
            break;
        }
    }
};

class AbstractBuilder
{
  public:
    virtual void createFile() = 0;
    virtual void buildFile_d_name(string name) = 0;
    virtual void buildFile_st_size(off_t size) = 0;
    virtual void buildFile_st_mtime(string time) = 0;

    virtual FileInfo *getFile() = 0;
};

class Builder : public AbstractBuilder
{
  public:
    void createFile()
    {
        FileInfo curFile;
    }
    void buildFile_d_name(string name)
    {
        curFile->fileName = name;
    }
    void buildFile_st_size(off_t size)
    {
        curFile->fileSize = size;
    }
    void buildFile_st_mtime(string time)
    {
        curFile->fileTime = time;
    }

    FileInfo *getFile()
    {
        return curFile;
    }

  private:
    FileInfo *curFile;
};

class Director
{
  public:
    Director(AbstractBuilder *builder)
    {
        curBuilder = builder;
    }

    void construct(string fileName, off_t fileSize, string fileTime)
    {
        if (!curBuilder)
        {
            return;
        }
        curBuilder->createFile();
        curBuilder->buildFile_d_name(fileName);
        curBuilder->buildFile_st_size(fileSize);
        curBuilder->buildFile_st_mtime(fileTime);
    }

  private:
    AbstractBuilder *curBuilder;
};


string changeSymble(string filename)
{
    /*
    将文件名特殊符号和空格转化为'_'
    */
    unsigned int pos;
    while ((pos = filename.find('/')) != string::npos || (pos = filename.find(':')) != string::npos || (pos = filename.find(' ')) != string::npos)
    {
        filename.replace(pos, 1, "_");
    }
    return filename;
}

//将遍历结果保存至日志文件
void saveLog(string dirName, vector<FileInfo> fileVector)
{
    chdir("./log");
    fstream outfile;
    outfile.open(changeSymble(dirName));
    vector<FileInfo>::iterator iter;
    for (iter = fileVector.begin(); iter != fileVector.end() - 1; iter++)
        outfile << changeSymble(iter->fileName) << "\t" << iter->fileSize << "\t" << iter->fileTime << endl;
    outfile << changeSymble(iter->fileName) << "\t" << iter->fileSize << "\t" << iter->fileTime << endl;
    outfile.close();
    chdir("..");
}

//从日志文件中读取文件信息
vector<FileInfo> readLog(string dirName)
{
    chdir("./log");
    fstream logfile;
    logfile.open(changeSymble(dirName));
    vector<FileInfo> logFileList;
    string fileName;
    off_t fileSize;
    string fileTime;
    if (logfile)
    {
        while (!logfile.eof())
        {
            logfile >> fileName;
            logfile >> fileSize;
            logfile >> fileTime;

            AbstractBuilder *builder = new Builder();
            Director *director = new Director(builder);
            director->construct(fileName, fileSize, fileTime);
            FileInfo *tf = builder->getFile();
            logFileList.push_back(*tf);
        }
        logfile.close();
    }
    else
    {
        cout << "No File" << endl;
    }
     chdir("..");
    return logFileList;
}

class MatchRegex
{
  public:
    int macth_regex(const char *buffer, const char *pattern)
    {
        regex_t reg;            // 定义一个正则实例，用来存放编译后的正则表达式
        regmatch_t pm[1] = {0}; // 定义匹配结果在带匹配串中的下标范围
        int ret = 0;
        char errbuf[1024] = {0};
        ret = regcomp(&reg, pattern, REG_EXTENDED | REG_ICASE); // 编译正则模式串
        // 编译执行不成功
        if (ret != 0)
        {
            regerror(ret, &reg, errbuf, sizeof(errbuf)); // 返回错误
            fprintf(stderr, "%s:regcom(%s)\n", errbuf, pattern);
            return -1;
        }
        // 匹配它，如果匹配上了
        if (regexec(&reg, buffer, 1, pm, 0) == 0)
        {
            regfree(&reg); // 释放正则表达式
            return 0;      //匹配成功
        }
        // 否则
        else
        {
            regfree(&reg);
            return -1;
        }
    }
};

//递归扫描目录
class ScanDirectory
{
  public:
    MatchRegex match;
    vector<FileInfo> scanDir(char *path, char *pattern)
    {
        int i, j;
        char file_path[512] = {0};
        char file[512] = {0};
        DIR *dir = NULL;           //定义一个指向目录的DIR结构体的指针，相当于句柄
        struct dirent *ptr = NULL; //定义一个指向 dirent 结构体的指针，指向目录下的所有文件
        struct stat buf;           // stat结构体，存储文件的详细信息
        // 如果文件打开不成功
        if ((dir = opendir(path)) == NULL)
        {
            perror("opendir failed!");
            return fileVector;
        }
        // 目录不为空
        while ((ptr = readdir(dir)) != NULL)
        {
            // 如果不是隐藏文件
            if (ptr->d_name[0] != '.')
            {
                strcpy(file_path, path);
                // 如果文件路径最后不带斜杠/,则加上去
                if (path[strlen(path) - 1] != '/')
                    strcat(file_path, "/");
                // 因为是递归扫描，所以给每一个文件构建完整的文件名
                strcat(file_path, ptr->d_name);
                // 当获取文件信息失败的时候终止程序运行
                assert(stat(file_path, &buf) != -1);
                // 如果是普通常规文件
                if (S_ISREG(buf.st_mode))
                {
                    // 匹配关键字
                    if (match.macth_regex(ptr->d_name, pattern) == 0)
                    {
                        // 匹配成功就放进vector
                        FileInfo fileInfo = {file_path, buf.st_size, ctime(&buf.st_mtime)};
                        fileVector.push_back(fileInfo);
                    }
                }
                // 如果是目录，则继续递归扫描
                else if (S_ISDIR(buf.st_mode))
                {
                    scanDir(file_path, pattern);
                }
            }
        }
        return fileVector;
    }
};

void printFileVector(vector<FileInfo> &fileVector)
{
    //输出文件
    printf("查找到以下相关文件:\n");
    vector<FileInfo>::iterator fileIter;
    for (fileIter = fileVector.begin(); fileIter != fileVector.end(); fileIter++)
    {
        cout << "文件名: ";
        cout << fileIter->fileName;
        cout << "  ";
        cout << "文件大小: ";
        cout << fileIter->fileSize;
        cout << "  ";
        cout << "最后修改时间: ";
        cout << fileIter->fileTime << endl;
    }
}

int main(int argc, char const *argv[])
{
    ScanDirectory scan;
    string logFileName;
    char path[512];
    char pattern[32];
    int sortBy;
    int modeID;
    char whetherNext;
    int next;
    while (true)
    {
        printf("请输入目录的遍历模式：(1.日志模式   2.差异模式  0.退出)\n");
        scanf("%d", &modeID);
        if (0 == modeID)
        {
            exit(0);
        }
        printf("请输入想要扫描的目录路径:\n");
        scanf("%s", path);
        printf("请输入想要扫描的文件关键字:\n");
        scanf("%s", pattern);
        printf("请输入排序规则(1.文件名 2.文件大小 3.文件修改时间)：\n");
        scanf("%d", &sortBy);
        //在排序前先扫描目录
        scan.scanDir(path, pattern);
        //    //扫描之后再对文件排序
        //    SortFactory *sortFactory = new SortFactory(sortBy);
        //    sortFactory->sortID->sortFile(fileVector);
        //    printFileVector(fileVector);

        if (1 == modeID)
        {
            logFileName = path;
            saveLog(logFileName, fileVector);
            //在排序前先扫描目录
            fileVector = scan.scanDir(path, pattern);
            //扫描之后再对文件排序
            SortFactory *sortFactory = new SortFactory(sortBy);
            sortFactory->sortID->sortFile(fileVector);
            if (fileVector.empty())
            {
                printf("---------------------------------------\n");
                printf("-        没有找到匹配的文件！         -\n");
                printf("---------------------------------------\n");
            }
            else
            {
                while (true)
                {
                    printFileVector(fileVector);
                    printf("在当前结果继续操作？Y(y)/N(n)\n");
                    scanf("%s", &whetherNext);
                    if ('y' == whetherNext || 'Y' == whetherNext)
                    {
                        printf("请选择操作内容:1.进一步排序 2.谓词筛选\n");
                        scanf("%d", &next);
                        if (1 == next)
                        {
                            printf("请输入排序规则(1.文件名 2.文件大小 3.文件修改时间)：\n");
                            scanf("%d", &sortBy);
                            sortFactory = new SortFactory(sortBy);
                            sortFactory->sortID->sortFile(fileVector);
                        }
                        else if (2 == next)
                        {
                            printf("请输入要搜索的文件关键字：\n");
                            scanf("%s", pattern);
                            fileVector = scan.scanDir(path, pattern);
                        }
                    }
                    else
                        break;
                }
            }
        }
        else
        {
            //差异模式
            // 从日志中获取文件信息
            vector<FileInfo> logFileList = readLog(logFileName);
            logFileList = scan.scanDir(path, pattern);

            // 更新搜索结果
            logFileName = path;
            saveLog(logFileName, fileVector);

            // 匹配关键字
            fileVector = scan.scanDir(path, pattern);

            // 排序
            SortFactory *sortFactory = new SortFactory(sortBy);
            sortFactory->sortID->sortFile(fileVector);
            sortFactory->sortID->sortFile(logFileList);

            printf("---------------------------------------\n");
            cout << "该目录文件差异情况如下：" << endl;
            vector<FileInfo>::iterator iter;
            for (iter = fileVector.begin(); iter != fileVector.end(); iter++)
            {
                cout.flags(ios::left);

                vector<FileInfo>::iterator log_iter;

                for (log_iter = logFileList.begin(); log_iter != logFileList.end(); log_iter++)
                {
                    if (iter->fileName == log_iter->fileName)
                    {
                        break;
                    }
                }

                if (log_iter == logFileList.end())
                {
                    cout << "当前(新增)"
                         << "   文件名：" << iter->fileName << "   文件大小：" << iter->fileSize
                         << "   文件修改时间：" << iter->fileTime << endl;
                }
                else if ((*log_iter) != (*iter))
                {
                    cout << "当前内容："
                         << "   文件名：" << iter->fileName << "   文件大小：" << iter->fileSize
                         << "   文件修改时间：" << iter->fileTime << endl;
                    cout << "日志内容："
                         << "   文件名：" << iter->fileName << "   文件大小：" << iter->fileSize << "   文件修改时间" << iter->fileTime << endl;
                    logFileList.erase(log_iter);
                }
                else
                {
                    logFileList.erase(log_iter);
                }
            }
            printf("---------------------------------------\n");
            logFileList.clear();
        }
        fileVector.clear();
    }
}
