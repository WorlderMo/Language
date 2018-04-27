#include <stdio.h>
int main(int argc, char const *argv[])
{
	int n,s[100],min,t;
	while(scanf("%d",&n) != EOF)
	{
		int k = 0;
		if (n != 0)
		{
			for (int i = 0; i < n; i++)
			{
				scanf("%d",&s[i]);
			}
			min = 0;
			for (int i = 0; i < n; i++)
			{
				if (s[i] <= s[min])
				{
					min = i;
				}
			}
			t = s[min];
			s[min] = s[0];
			s[0] = t;
			for (int i = 0; i < n; i++)
			{
				/*if(k == 1)
					printf(" ");
				printf("%d",s[i] );
				k=1;*/
				printf("%d",s[i]);
				printf(i==n-1?"\n":" ");
			}
			//printf("\n");
		}
	}
	return 0;
}