#include <stdio.h>
#include <math.h>
#define PI 3.1415927
int main(int argc, char const *argv[])
{
	double r,v,d;
	while(scanf("%lf",&r)!=EOF)
	{
		d=pow(r,3);
		v=4.0/3*PI*d;
		printf("%.3f\n",v);
	}
	return 0;
}