#include <stdio.h>
int main(int argc, char const *argv[])
{
	int n;
	while(scanf("%d",&n)!=EOF)
		{
			int s=1;
			for (int i = 1; i <= n-1; i++)
			{
				s = (s+1)*2;
			}
			printf("%d\n",s );
		}
	return 0;
}