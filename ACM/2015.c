#include <stdio.h>
int main(int argc, char const *argv[])
{
	int n,m,s[100];
	while(scanf("%d%d",&n,&m)!=EOF)
	{
		int k=0,sum=0,a=0,b=0;
		for (int i = 1; i <= n; i++)
		{
			s[i] = 2*i;
		}
		for (int i = 0; i < n/m; i++)
		{
			for (int j = m*i+1; j < (i+1)*m+1; j++)
			{
				sum+=s[j];
			}
			if (b==1)
				printf(" ");
			printf("%d",sum/m );
			b = 1;
			k++;
			sum=0;
		}
		sum = 0;
		if (n%m !=0 )
		{
			for (int i = m*k+1; i <= n; ++i)
				{
					sum+=s[i];
				}
			a = n%m;
			printf(" ");
			printf("%d", sum/a);
		}
		printf("\n");
	}
	return 0;
}