#include <stdio.h>

void QuickSort(int s[], int left, int right)
{
	int i, j, key;
	i = left;
	j = right;
	key = s[i];    //把一个数作为基准值,用于分组的依据,一般选第一个数,而且用来保存这个数
	while(i < j)
	{
	    while(i < j && key < s[j])  //依次找出右边小于基准值的数据,每次j减一,直到找到为止
	    {
	    	j--;
	    }
	    if(i < j)     //到这一步说明已经找到比基准值小的数了,把它和基准值交换位置,i++到下一个元素
	    {
	    	s[i] = s[j];
	    	i++;
	    }
	    while(i < j && key >= s[i])
	    {
	        i++;
	    }
	    if(i < j)
	    {
	    	s[j] = s[i];
	    	j--;
	    }
	}
	s[i] = key;   //此时i=j
	if(left < i)  //设置递归退出的条件
	{
		QuickSort(s, left, i-1);
	}
	if(i < right)
	{
		QuickSort(s, i+1, right);
	}
}

int main(int argc, char const *argv[])
{
	int i, left, right, s[10];
	printf("请输入10个数字：\n");
	for(i=0; i<10; i++)
	{
		scanf("%d", &s[i]);
	}
	printf("请输入数组的最左边的下标left和最右边的下标right：\n");
	scanf("%d %d", &left, &right);
	QuickSort(s, left, right);
	printf("快速排序后的数字顺序为：\n");
	for(i=0; i<10; i++)
	{
		if(i==0)
		{
			printf("%d", s[i]);
		}
		else
		{
			printf("%4d", s[i]);
		}
	}
	printf("\n");
	return 0;
}