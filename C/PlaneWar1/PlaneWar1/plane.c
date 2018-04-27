#include "plane.h"
char g_PlaneBack[BACK_Y][BACK_X] = {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
									1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
									1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
									1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
									1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
									1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
									1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
									1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
									1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
									1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
									1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
									1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
									1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
									1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
									1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
									1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
									1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
									1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
									1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
									1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
									};

char g_PlaneBackTemp[BACK_Y][BACK_X] = {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
};



int g_heroX = 10;
int g_heroY = 17;

struct _Node *g_pHead = NULL;
struct _Node *g_pEnd = NULL;

int g_score = 0;

//显示子弹
//void ShowDan()
//{
//	struct _Node* pTemp = g_pHead;
//
//	while (pTemp)
//	{
//		//GotoXY(pTemp->y, pTemp->x);
//		//printf("弹");
//		
//
//		pTemp = pTemp->pNext;
//	}
//	
//}
//计分
void Score()
{
	GotoXY(10, 25);
	printf ("得分：%d",g_score*10);
}

//消除子弹
void DeleteDan()
{
	struct _Node* pTemp = g_pHead;

	g_pHead = g_pHead->pNext;
	free(pTemp);
}
//飞机碰撞
void DeletePlane()
{
	struct _Node* pTemp = g_pHead;

	while (pTemp)
	{
		//判断与飞机的位置
		if (3 == g_PlaneBackTemp[pTemp->y][pTemp->x])
		{
			struct _Node* pTemptp = pTemp;

			g_PlaneBack[pTemp->y][pTemp->x] = 0;
			
			pTemp = pTemp->pNext;
			g_score++;
			Score();
			//删除当前节点 pTemptp  
			DeleteNode(pTemptp);
			//进行下一次循环
			continue;
		}

		pTemp = pTemp->pNext;
	}
}
//删除链表指定的节点
void DeleteNode(struct _Node* p)
{
	//检测参数
	if (NULL == p)
	{
		return ;
	}
	//检测链表
	if (NULL == g_pHead)
	{
		return ;
	}

	//删除节点  只有一个节点
	if (g_pHead == g_pEnd)
	{
		if (p == g_pHead)
		{
			free(g_pHead);
			g_pHead = NULL;
			g_pEnd = NULL;
		}
	} //有两个节点
	else if (g_pHead->pNext == g_pEnd)
	{
		//头还是尾巴
		if (p == g_pHead)
		{
			free(g_pHead);
			g_pHead = g_pEnd;
			g_pHead->pNext = NULL;
		}
		if (p == g_pEnd)
		{
			free(g_pEnd);
			g_pEnd = g_pHead;
			g_pHead->pNext = NULL;
		}	
	} //多个节点 >2
	else
	{
		//删除的头
		if (p == g_pHead)
		{
			struct _Node* pTemp = g_pHead;
			g_pHead = g_pHead->pNext;
			free(pTemp);
		}
		else if (p == g_pEnd)
		{
			struct _Node* pTemp = g_pHead;
			while (pTemp)
			{
				if (pTemp->pNext == p)
				{
					g_pEnd = pTemp;
					pTemp->pNext = p->pNext;
					free(p);
				}

				pTemp = pTemp->pNext;
			}
		}
		else
		{
			//找到删除节点的前一个
			struct _Node* pTemp = g_pHead;
			while (pTemp)
			{
				if (pTemp->pNext == p)
				{
					pTemp->pNext = p->pNext;//  183 7879 447
					free(p);
				}

				pTemp = pTemp->pNext;
			}
		}
	}
}

//子弹动起来
void DanRun()
{
	struct _Node* pTemp = g_pHead;

	//链表检测
	if (NULL == g_pHead)
		return ;

	//边界碰撞
	if (1 == g_pHead->y)
	{
		g_PlaneBack[g_pHead->y][g_pHead->x] = 0;
		DeleteDan();
	}
	

	//遍历链表，子弹移动
	pTemp = g_pHead;
	while (pTemp)
	{
		//原位置子弹清空
		g_PlaneBack[pTemp->y][pTemp->x] = 0;
	
		pTemp->y-- ;
		//到边界就别减了， 再减越界了
		if (pTemp->y < 1)
			pTemp->y = 1;

		//新位置子弹
		g_PlaneBack[pTemp->y][pTemp->x] = 4;

		pTemp = pTemp->pNext;
	}
	
	//飞机碰撞消除
	DeletePlane();
}

//子弹链表尾添加
void InsertDan(int y, int x)
{
	//创建节点
	struct _Node *pTemp = (struct _Node*)malloc(sizeof(struct _Node));

	//节点成员初始化
	pTemp->y = y;
	pTemp->x = x;
	pTemp->pNext = NULL;

	//链接
	if (NULL == g_pHead)
	{
		g_pHead = pTemp;
		//g_pEnd = pTemp;
	}
	else
	{
		g_pEnd->pNext = pTemp;	
	}
	g_pEnd = pTemp;
}
//
//飞机下落
void PlaneDown()
{
	int i, j;
	
	for (i = BACK_Y-2; i > 1; i--)
	{
		for (j = 1; j < BACK_X-1; j++)
		{
			//遇到子弹和 英雄飞机，就不用下落了
			if (2 == g_PlaneBack[i-1][j] || 4 == g_PlaneBack[i-1][j] ) //飞机子弹不能咯
				continue;

			g_PlaneBack[i][j] = g_PlaneBack[i-1][j];
		}
	}

	//产生新的敌人飞机
	ReducePlane();
}

//产生飞机
void ReducePlane()
{
	int i = 0;
	//种子
	srand((unsigned int)clock());

	//第一行清空
	for (i = 0; i < BACK_X -1; i++)
	{
		g_PlaneBack[1][i] = 0;
	}

	//随机位置产生飞机
	for (i = 0; i < BACK_X-1; i++)
	{
		int j = rand()%10; 
		
		if (0 == j)
		{
			g_PlaneBack[1][i] = 3;//赋值飞机
		}
	}
}

//封面
void FengMian()
{
	printf ("\n\n\n\t\t\t        《欢迎来到飞机世界》\n");
	printf ("\n\t\t\t      《本程序由莫海浪LNN所有》\n");
	printf ("\n\t\t\t《 W A S D,控制飞机方向, 空格键放炮》\n");
	printf ("\n\t\t\t        《 按任意键键继续 》\n");
}

//打印
void PrintfBack1()
{
	int i,
		j;
	//兼容性背景
	char strBackTemp[BACK_Y][BACK_X*2 + 2] = {0};
	char strBackTemp2[BACK_Y*(BACK_X*2 + 2)] = {0};
	//设置英雄的位置
	SetHeroPos();

	//装背景
	for (i = 0; i < BACK_Y; i++)
	{
		for (j = 0; j < BACK_X; j++ )
		{
			switch(g_PlaneBack[i][j])
			{
			case 0:
				strcat(strBackTemp[i], "  "); //
				break;
			case 1:
				strcat(strBackTemp[i], "■");
				break;
			case 2:
				strcat(strBackTemp[i], "士");
				break;
			case 3: //敌人飞机
				break;
			}
		}
		strcat(strBackTemp[i], "\n");
	}

	//打印背景
	for (i = 0; i < BACK_Y; i++)
	{
		//printf (strBackTemp[i]);
		strcat(strBackTemp2, strBackTemp[i]);
	}
	//打印一次
	printf (strBackTemp2);
}

//设置鼠标在控制台的位置
void GotoXY(int y, int x)
{
	COORD rd;
	rd.Y = y;
	rd.X = x*2;
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), rd);
}

void PrintfBack()
{
	int i,
		j;
	
	//设置英雄的位置
	SetHeroPos();

	//装背景
	for (i = 1; i < BACK_Y-1; i++)
	{
		for (j = 1; j < BACK_X-1; j++ )
		{
			GotoXY(i, j);

			switch(g_PlaneBack[i][j])
			{
			case 0:
				printf ("  ");  //控制台清空
				break;
			case 1:
				//printf ("■");
				break;
			case 2:
				printf ("士");
				break;
			case 3://敌人飞机
				printf ("诺");
				break;
			case 4:
				printf ("浪");
				break;
			}
		}
	}
}

//设置英雄的位置
void SetHeroPos()
{
	g_PlaneBack[g_heroY][g_heroX] = 2;
}

//控制英雄移动
void HeroPlay() //GetAsyncKeyState
{
	//记录数组
	memcpy(g_PlaneBackTemp[0], g_PlaneBack[0], BACK_X*BACK_Y);

	if (g_heroY > 1 && GetAsyncKeyState('W'))
	{
		//走到英雄的位置
		GotoXY(g_heroY, g_heroX);
		//英雄旧的位置清空
		g_PlaneBack[g_heroY][g_heroX] = 0;
		//空格替换掉 士
		printf("  ");

		g_heroY--;
	}
	if (g_heroY < BACK_Y - 2 && GetAsyncKeyState('S'))
	{
		//同上
		GotoXY(g_heroY, g_heroX);
		g_PlaneBack[g_heroY][g_heroX] = 0;
		printf("  ");

		g_heroY++;
	}

	if ( g_heroX > 1 && GetAsyncKeyState('A') )
	{
		//同上
		GotoXY(g_heroY, g_heroX);
		g_PlaneBack[g_heroY][g_heroX] = 0;
		printf("  ");
		
		g_heroX--;
	}
	if (g_heroX < BACK_X - 2 && GetAsyncKeyState('D'))
	{
		//同上
		GotoXY(g_heroY, g_heroX);
		g_PlaneBack[g_heroY][g_heroX] = 0;
		printf("  ");
		
		g_heroX++;
	}
	if (GetAsyncKeyState(VK_SPACE)&1)
	{
		//产生子弹
		InsertDan(g_heroY, g_heroX);
	}

	//判断英雄死亡
}

BOOL IsHeroDie1()
{
	if (3 == g_PlaneBackTemp[g_heroY][g_heroX])
	{
		//撞了
		return false;
	}

	return true;
}