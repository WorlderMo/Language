#include <stdio.h>
#include <math.h>
int main(int argc, char const *argv[])
{
	double i,j;
	while(scanf("%lf",&i)!=EOF)
	{
		j=fabs(i);
		printf("%.2f\n",j);
	}
	return 0;
}