#include <stdio.h>
int main(int argc, char const *argv[])
{
	int n,m,a,b,c;
	while(scanf("%d%d",&n,&m)!=EOF)
	{
		int k=0;
		for (int i = n; i <= m; i++)
		{
			a = i/100;
			b = (i%100)/10;
			c = i%10;
			if(i==(a*a*a+b*b*b+c*c*c))
			{
				if (k==1)
					printf(" ");
				printf("%d", i );
				k=1;
			}
		}
		if (k==0)
		{
			printf("no\n");
		}
		else
			printf("\n");
	}
	return 0;
}