#include <stdio.h>
int main(int argc, char const *argv[])
{
	int n;
	while(scanf("%d",&n)!=EOF)
	{
		int s[100],a;
		float sum = 0.0;
		for (int i = 0; i < n; i++)
		{
			scanf("%d",&s[i]);
		}
		for (int i = 0; i < n-1; i++)
		{
			for (int j = i+1; j < n; j++)
			{
				if (s[i]>s[j])
				{
					a = s[j];
					s[j] = s[i];
					s[i] = a;
				}
			}
		}
		for (int j = 1; j < n-1; j++)
		{
			sum += s[j];
		}
		printf("%.2f\n",sum/(n-2) );
	}
	return 0;
}
/*还有另一种更简便方法：
#include<stdio.h>
int main()
{
	int a[100],n,i,j,max,min;
	double sum,ave;
	while(scanf("%d",&n)!=EOF)
	{
		sum=0;
		for(i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
		}
		min=a[0];
		max=a[0];
		for(i=0;i<n;i++)
		{

			max=a[i]>max?a[i]:max;
			min=a[i]<min?a[i]:min;
			sum+=a[i];
		}
		ave=(sum-min-max)/(n-2);
		printf("%.2f\n",ave);
	}
	return 0；
}*/