#include <stdio.h>
#include <math.h>
int main(int argc, char const *argv[])
{
	int m,n[1000];
	float s,a;
	while(scanf("%d",&m)!=EOF)
	{
		for (int i = 0; i < m; i++)
		{
			s=0.0;
			scanf("%d",&n[i]);
			for (int j = 1; j <= n[i]; j++)
			{
				a=pow(-1,j+1);
				s+=a*1/j;
			}
			printf("%.2f\n",s );
		}
	}
	return 0;
}
