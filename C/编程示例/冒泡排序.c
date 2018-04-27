#include <stdio.h>

void BubbleSort(int s[], int n)
{
	int i, j, temp;
	for(i=0; i<n-1; i++)
	{
		for(j=n-1; j>i; j--)
		{
			if(s[j] < s[j-1])
			{
				temp = s[j-1];
				s[j-1] = s[j];
				s[j] = temp;
			}
		}
	}
}

int main(int argc, char const *argv[])
{
	int s[10], i;
	printf("������ʮ�����ݣ�\n");
	for(i=0; i<10; i++)
	{
		scanf("%d", &s[i]);
	}
	BubbleSort(s, 10);
	printf("ð��������������˳��Ϊ��\n");
	for(i=0; i<10; i++)
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
	printf("\n");
	return 0;
}
