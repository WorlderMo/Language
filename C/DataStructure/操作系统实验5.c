#include <stdio.h>
#include <stdlib.h>

#define MINSIZE 1    //不再分割的最小分区大小
#define REQUEST 1    //作业申请空间
#define FREE    2    //作业释放空间

typedef struct memory_info
{
	int address;  //起始地址
	int size;     //大小
	int ID;	  //若空闲，则为0，若被占用，则为作业的ID，可以根据ID在释放内存时找到这个分区
	int state;    //是否空闲
	struct memory_info *prior;
	struct memory_info *next;
}memoryList;

memoryList *L;    //空闲分区链
int memory_num = 0;

//作业请求序列结构体
typedef struct job_info
{
	int ID;
	int state;   //0表示申请，1表示释放
	int size;    //申请或者释放多少内存
}JOB;

//初始化空闲分区链为一个双向链表，头结点为L
int InitList()
{
	L = (memoryList *)malloc(sizeof(memoryList)); //L为头结点，执行这一步时，linux会把L->state默认初始化为0，windows不会！
	memoryList *first = (memoryList *)malloc(sizeof(memoryList));  //first为第一个结点

	L->next = first;
	L->prior = NULL;
	first->next = NULL;
	first->prior = L;
	first->address = 0;
	first->size = memory_num;
	first->ID = 0;
	first->state = 0;
	return 0;
}
//按地址递增从头找到尾，找到合适的就分配
int alloc_firstfit(JOB *job)
{
	memoryList *p = L->next;
	while(p != NULL)
    	{
		if(p->state == 0&&p->size>job->size)
		{
            if(p->size-job->size <= MINSIZE)
			{
               	p->state = 1;		//直接把这个分区分配给该作业
				p->ID = job->ID;		//记录这个分区分配给哪个作业
           		}
			else		//从分区中划出job->size大小的分区，并修改有关数据结构
			{
                memoryList *t = (memoryList *)malloc(sizeof(memoryList));
				t->address = p->address+job->size;
                t->size = p->size-job->size;
               	t->state = 0;
				t->ID = 0;
				t->prior = p;
                t->next = p->next;
                if(p->next != NULL)
				{
                    p->next->prior = t;
                }
               	p->next = t;
                p->size = job->size;
                p->state = 1;
				p->ID = job->ID;
			}
			break;
        	}
		p = p->next;
    	}
	return 0;
}
//找能满足作业大小，且是最小的分区块
int alloc_bestfit(JOB *job)
{
	int minSize = 640;
	memoryList *p = L->next;
	memoryList *min = NULL;		//min指向最小的分区
	while(p != NULL)			//找到能分给作业的最小空闲结点
	{
		if(p->state == 0&&p->size>job->size&&p->size <= minSize)
		{
			minSize = p->size;
			min = p;
		}
		p = p->next;
	}
	if(min->size-job->size <= MINSIZE)
	{
		min->state = 1;		//直接把这个分区分配给该作业
		min->ID = job->ID;		//记录这个分区分配给哪个作业
	}
	else		//从分区中划出job->size大小的分区，并修改有关数据结构
	{
		memoryList *t = (memoryList *)malloc(sizeof(memoryList));
		t->address = min->address+job->size;
		t->size = min->size-job->size;
		t->state = 0;
		t->ID=0;
		t->prior = min;
		t->next = min->next;
		if(min->next != NULL)
		{
			min->next->prior = t;
		}
		min->next = t;
		min->size = job->size;
		min->state = 1;
		min->ID = job->ID;
	}
	return 0;
}
//检验方法之一：不能有两个空闲分区相邻
int freeNode(JOB *job)
{
	memoryList *p = L->next;
	while(p != NULL)
	{
		if(p->ID == job->ID)//找到这个节点
		{
			//第一种情况：前一相邻分区空闲，后一分区被占用或没有后一分区
			if((p->prior->state == 0&&p->next->state == 1&&p->prior != L)||
				(p->prior->state == 0&&p->next == NULL&&p->prior != L))
			//！！切记，凡是用到p->prior->state初始化为0，而windows不会state==0
			{
				p->prior->size = p->prior->size+p->size;
				p->prior->next = p->next;
				if(p->next != NULL)
				{
					p->next->prior = p->prior;
				}
			}
		 	//第二种情况：后一相邻分区空闲，前一分区被占用或是头结点
			else if((p->next->state == 0&&p->prior->state == 1)||(p->next->state == 0&&p->prior == L))
			{
				p->ID = 0;
				p->state = 0;
				p->size = p->size+p->next->size;
				if(p->next->next != NULL)
				{
					p->next->next->prior = p;
				}
				p->next = p->next->next;
			}
			//第三种情况：前后分区都空闲
			else if(p->prior->state == 0&&p->next->state == 0)
			{
				p->prior->size = p->prior->size+p->next->size+p->size;
				p->prior->next = p->next->next;
				if(p->next->next != NULL)
				{
					p->next->next->prior = p->prior;
				}
			}
			//第四种情况：前后分区都不空闲
			else
			{
				p->ID = 0;
				p->state = 0;
			}
			break;
		}
	p = p->next;
}
	return 0;
}
int print()
{
	printf("\n执行后的状态图如下\n\n");
	memoryList *p = L->next;
	printf("---------------------------------------------\n");
	printf("  %-10s%-10s%-20s%-10s\n", "address","size","ID(0为空闲）", "state");
	while(p != NULL)
	{
	    printf("---------------------------------------------\n");
		printf("  %-10d%-10d%-20d%-10d\n", p->address,p->size,p->ID,p->state);
		p = p->next;
	}
	printf("---------------------------------------------\n");
	return 0;
}

int main()
{
	//根据题目所给数据，定义一个作业序列数组
	JOB job;
	int option;		//选择首次适应算法还是最佳适应算法
	printf("-------------------------------------------------\n");
	printf("            请选择动态分区分配算法               \n");
	printf("                1.首次适应算法                   \n");
	printf("                2.最佳适应算法                   \n");
	printf("                0.退出程序                       \n");
	printf("-------------------------------------------------\n");
	scanf("%d", &option);
	if(option == 1)     //执行首次适应算法
	{
		printf("\n");
		printf("------------------------------------------------\n");
		printf("         以下是首次适应算法的执行过程:          \n");
		printf("------------------------------------------------\n");
		printf("\n请输入初始可用总内存大小:\n");
		scanf("%d", &memory_num);
		printf("\n正在为你分配内存，请稍候...\n");
		InitList();		//初始化空闲分区链
		print();
		printf("\n输入1表示申请内存，输入2表示释放内存，输入0退出\n");
		while((scanf("%d", &job.state)) && (job.state != 0))
		{

			if(job.state == REQUEST)	//申请内存空间，调用首次适应算法
			{
				printf("\n请输入要申请内存空间的作业ID:\n");
				scanf("%d", &job.ID);
				printf("\n请输入此作业的内存空间\n");
				scanf("%d", &job.size);
				if(job.size > memory_num)
				{
					printf("\n对不起，所申请的内存空间大于可用内存空间！\n");
					printf("\n分配空间失败！\n");
				}
				else
				{
					printf("\n正在为作业%d申请%dKB，请稍候...\n", job.ID,job.size);
					alloc_firstfit(&job);
					print();
				}
			}
			if(job.state == FREE)		//释放内存空间，回收内存
			{
				printf("\n请输入要释放内存空间的作业ID:\n");
				scanf("%d", &job.ID);
				printf("\n请输入此作业要释放的内存空间\n");
				scanf("%d", &job.size);
				printf("\n正在为作业%d释放%dKB，请稍候...\n", job.ID,job.size);
				freeNode(&job);
				print();
			}
			printf("\n输入1表示申请内存，输入2表示释放内存，输入0退出\n");
		}
	}
	else if(option == 2)      //执行最佳适应算法
	{
		printf("\n");
		printf("------------------------------------------------\n");
		printf("         以下是最佳适应算法的执行过程:          \n");
		printf("------------------------------------------------\n");
		printf("\n请输入初始可用总内存大小:\n");
		scanf("%d", &memory_num);
		printf("\n正在为你分配内存，请稍候...\n");
		InitList();		//初始化空闲分区链
		print();
		printf("\n输入1表示申请内存，输入2表示释放内存，输入0退出\n");
		while((scanf("%d", &job.state)) && (job.state != -1))
		{
			if(job.state == REQUEST)		//申请内存空间，调用最佳适应算法
			{
				printf("\n请输入要申请内存空间的作业ID:\n");
				scanf("%d", &job.ID);
				printf("\n请输入此作业要申请的内存空间\n");
				scanf("%d", &job.size);
				printf("\n正在为作业%d申请%dKB，请稍候...\n", job.ID,job.size);
				alloc_bestfit(&job);
				print();
			}
			if(job.state == FREE)			//释放内存空间，回收内存
			{
				printf("\n请输入要释放内存空间的作业ID:\n");
				scanf("%d", &job.ID);
				printf("\n请输入此作业要释放的内存空间\n");
				scanf("%d", &job.size);
				printf("\n正在为作业%d释放%dKB，请稍候...\n", job.ID,job.size);
				freeNode(&job);
				print();
			}
			printf("\n输入1表示申请内存，输入2表示释放内存，输入0退出\n");
		}
	}

	return 0;
}
