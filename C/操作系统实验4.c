#include <stdio.h>

typedef struct PCB
{
    int id;
    int priority;
    int cputime;
    int alltime;
    char *state;
}PCB;

PCB p[5] = {
                {  0,  9,  0,  3,  "READY"},
                {  1, 38,  0,  3,  "READY"},
                {  2, 30,  0,  6,  "READY"},
                {  3, 29,  0,  3,  "READY"},
                {  4,  0,  0,  4,  "READY"}
           };  //设置5个进程的PCB

int i;
int runtime = 0;  //表示cpu运行的时间
int ready_count;  //表示统计就绪队列中的进程数
int ready_queue[5] = { -1, -1, -1, -1, -1};  //用于存储排序后的就绪队列的ID号

//用于查找优先数最大的进程ID
int maxPriority()
{
    int tag;
    int max;
    for (i = 0; i < 5; i++ )
    {
        if ("END" != p[i].state)
        {
            max = p[i].priority;
            tag = i;
            break;
        }

    }
    for (i = 0; i < 5; i++)
    {
        if (("END" != p[i].state) && (max < p[i].priority))
        {
            max = p[i].priority;
            tag = i;
        }
    }
    return p[tag].id;
}

//用于快速排序
int partition(int left, int right)
{
    int pivotKey = p[ready_queue[left]].priority;
    int pivotId = ready_queue[left];

    while (left < right)
    {
        while (left < right && p[ready_queue[right]].priority <= pivotKey)
        {
            right--;
        }
        ready_queue[left] = ready_queue[right];
        while (left < right && p[ready_queue[left]].priority >= pivotKey)
        {
            left++;
        }
        ready_queue[right] = ready_queue[left];
    }
    ready_queue[left] = pivotId;
    return left;
}

//快速排序算法
int quick_sort(int left, int right)
{
    if (left >= right)
    {
        return 0;
    }
    int pivotPos = partition(left, right);
    quick_sort(left, pivotPos - 1);
    quick_sort(pivotPos + 1, right);
 }

 //计算就绪队列
int get_ready_queue()
{
    ready_count = 0;
    for (i = 0; i < 5; i++)
    {
        if ("READY" == p[i].state)
        {
            ready_queue[ready_count] = p[i].id;
            ready_count++;
        }
    }
    quick_sort(0, ready_count - 1); //使用快速排序法对就绪队列进行排序
    return 0;
 }

 //打印五个进程的PCB
int printPCB()
{
    get_ready_queue();
    printf("RUNTIME: %d\n", runtime);
    printf("RUNNING PROGRAM:");
    for (i = 0; i < 5; i++)
    {
        if ("RUNNING" == p[i].state)
        {
            printf("ID%d\n", p[i].id);
            break;
        }
    }
    if (5 == i)   //没有正在运行的进程
    {
        printf("\n");
    }
    printf("READY_QUEUE:");
    for (i = 0; i < ready_count; i++)
    {
        printf("->ID%d", ready_queue[i]);
    }
    printf("\n");
    for (i = 0; i < 60; i++)
        printf("=");
    printf("\n");
    printf("ID          %-10d%-10d%-10d%-10d%-10d\n",
        p[0].id, p[1].id, p[2].id, p[3].id, p[4].id);

    printf("PRIORITY    %-10d%-10d%-10d%-10d%-10d\n",
        p[0].priority, p[1].priority, p[2].priority, p[3].priority,p[4].priority);

    printf("CPUTIME     %-10d%-10d%-10d%-10d%-10d\n",
        p[0].cputime, p[1].cputime, p[2].cputime, p[3].cputime, p[4].cputime);

    printf("ALLTIME     %-10d%-10d%-10d%-10d%-10d\n",
        p[0].alltime, p[1].alltime, p[2].alltime, p[3].alltime, p[4].alltime);

    printf("STATE       %-10s%-10s%-10s%-10s%-10s\n",
        p[0].state, p[1].state, p[2].state, p[3].state, p[4].state);

    return 0;
}

//模拟进程的运行过程，即时间片执行一次所进行的操作
void run()
{
    for (i = 0; i < 5; i++)
    {
        //该进程已运行结束
        if ("END" == p[i].state)
            {
                continue;
            }
        //该进程正在运行
        if ("RUNNING" == p[i].state)
        {
            p[i].cputime++;
            p[i].alltime--;
            if (0 != p[i].alltime)
            {
                p[i].priority -= 3;
                p[i].state = "READY";
            }
            else
            {
                p[i].priority = -1;
                p[i].state = "END";
            }
        }
    //该进程处于就绪状态
    else
        {
            p[i].priority++;
        }
    }
 }

int main()
{
    int end_count = 0;     //用于统计已运行结束的进程数
    int max;      //用于统计优先数最大的进程id

    for (i = 0; i < 5; i++)
    {
        if (0 == p[i].alltime)
        end_count++;
    }

    printf("进程初始状态如下:\n");
    printPCB();
    printf("请按回车键执行下一个时间片");
    getchar();
    printf("\n");

    while (1)
    {
        if (5 == end_count)    //五个进程都已运行结束
        {
            break;
        }
        runtime++;   //CPU时间片加1
        max = maxPriority();  //返回优先级最大的进程的ID
        p[max].state = "RUNNING";
        printPCB();
        run();
        if ("END" == p[max].state)
        {
            end_count++;
        }
        printf("请按回车键执行下一个时间片");
        getchar();
        printf("\n");
    }
    runtime++;
    printPCB();
    printf("所有进程已执行完毕\n");
    return 0;
}
