#include <stdio.h>
#include <stdlib.h>
#include <string.h>


#define MAXSIZE 200
#define OK 1
typedef int KeyType;
typedef int status;

typedef struct
{
	KeyType r[MAXSIZE + 1];  //r[0]闲置或用作哨兵单元
	int length;  //顺序表长度
}SqList;  //顺序表类型

status CreatList( SqList *L )
{
	L->r[0] = 0;
	printf( "请输入你的数组长度：\n" );
	scanf( "%d", &L->length );
	printf( "请输入你的数组元素：\n" );
	for ( int i = 1; i <= L->length; i++ )
	{
		getchar();
		scanf("%d", &L->r[i]);
	}
	// printf( "请确认你的数组元素:\n" );
	// for ( int j = 1; j <= L->length; j++ )
	// {
	// 	printf( "%c", L->r[j] );
	// 	printf( " " );
	// }
	return OK;
}

void BInsertSort( SqList L )  //对顺序表L作折半插入排序
{
	int low, high, mid;
	for ( int i = 2; i <= L.length; ++i )
	{
		L.r[0] = L.r[i];  //将L.r[i]暂存到L.r[0]
		low = 1;
		high = i - 1;
		while ( low <= high )  //在人[low..high]中折半查找有序插入的位置
		{
			mid = (low + high) / 2;  //折半
			if ( L.r[0] < L.r[mid] )
				high = mid - 1;  //插入点在低半区
			else
				low = mid + 1;  //插入点在高半区
		}
		for ( int j = i - 1; j >= high + 1; --j )
			L.r[j + 1] = L.r[j];  //记录后移
		L.r[high + 1] = L.r[0];  //插入
	}
	printf( "\n经过折半插入排序后的数组为：\n" );
	for ( int j = 1; j <= L.length; j++ )
	{
		printf( "%d", L.r[j] );
		printf( " " );
	}
}

int main()
{
	SqList L;
	CreatList(&L);
	BInsertSort(L);
	return 0;
}
