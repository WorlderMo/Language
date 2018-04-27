#include <stdio.h>

void shellsort(int s[], int n)  //希尔排序函数
{
	int i, gap, temp;
	for(gap=n/2; gap>0; gap/=2)
	{
		for(i=gap; i<n; i++)
		{
			temp = s[i];     //设置哨兵
			while(temp < s[i-gap] && i-gap >= 0)  //如果用s[0]作为哨兵，那么i-gap>=0可以省略
			{
				s[i] = s[i-gap];
				i -= gap;
			}
			s[i] = temp;
		}
	}
}

int main(int argc, char const *argv[])
{
	int i, s[10];
	printf("请输入10个数字：\n");
	for (i = 0; i < 10; i++)
	{
		scanf("%d", &s[i]);
	}
	printf("希尔排序后的数据为：\n");
	shellsort(s, 10);
	for (i = 0; i < 10; i++)
	{
		if(i == 0)
		{
			printf("%d", s[i]);
		}
		else
		{
			printf("%4d", s[i]);
		}
	}
	return 0;
}