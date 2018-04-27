#include <stdio.h>

void insort(int s[], int n)
{
	int i;
	for(i=2; i<=n; i++)
	{
		s[0] = s[i];     //设置哨兵
		while(s[0] < s[i-1] && i > 0)
		{
			s[i] = s[i-1];    //如果小于则交换位置
			i--;
		}
		s[i] = s[0];
	}
}
int main(int argc, char const *argv[])
{
	int s[11], i;
	printf("请输入10个数字：\n");
	for(i=1; i<11; i++)
	{
		scanf("%d", &s[i]);
	}
	insort(s, 10);
	printf("排序后的数字顺序为：\n");
	for(i=1; i<11; i++)
	{
		if(i==1)
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