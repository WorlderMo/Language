#include <stdio.h>
int main(int argc, char const *argv[])
{
	int s,x,y;
	while(scanf("%d%d",&x,&y)!=EOF)
	{
		if(x==0&&y==0)
			break;
		else
		{
			int k=0;
			for (int n = x; n <= y; n++)
			{
				s = n*n+n+41;
				for (int i = 2; i < s; i++)
				{
					if(s%i == 0)
					{
						k=1;
					}
				}
				if(k==1)
					break;
			}
			if(k==0)
				printf("OK\n");
			else
				printf("Sorry\n");
		}
	}
	return 0;
}