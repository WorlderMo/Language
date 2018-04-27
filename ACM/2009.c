#include <stdio.h>
#include <math.h>
int main(int argc, char const *argv[])
{
	double n,m,s[1000],sum;
	while(scanf("%lf%lf",&n,&m)!=EOF)
	{
		sum=0;
		s[0] = n;
		s[1] = sqrt(n);
		for (int i = 2; i < m; i++)
		{
			s[i]=sqrt(s[i-1]);
		}
		for (int j = 0; j < m; j++)
		{
				sum+=s[j];
		}
		printf("%.2f\n",sum );
	}
	return 0;
}