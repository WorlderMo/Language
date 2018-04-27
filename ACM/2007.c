#include <stdio.h>
int main(int argc, char const *argv[])
{
	int n,m;
	while(scanf("%d%d",&n,&m)!=EOF)
	{
		int x=0,y=0;
		if(n<=m)
		{
			for (int i = n; i <= m; i++)
			{
				if(i%2 == 0)
					x = x + (i*i);
				else
					y = y + (i*i*i);
			}
		}
		if(n>m)
		{
			for (int j = m; j <= n; j++)
			{
				if(j%2==0)
					x = x + (j*j);
				else
					y = y + (j*j*j);
			}
		}
		printf("%d %d\n",x,y);
	}
	return 0;
}