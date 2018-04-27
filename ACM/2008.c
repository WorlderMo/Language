#include <stdio.h>
int main(int argc, char const *argv[])
{
	int n,a,b,c;
	float s[100];
	while(scanf("%d",&n)!=EOF)
	{
		a=0,b=0,c=0;
		if(n!=0)
		{
			for (int i = 0; i < n; i++)
			{
				scanf("%f",&s[i]);
				if(s[i]>0.0)
					c++;
				if(s[i]==0.0)
					b++;
				if(s[i]<0.0)
					a++;
			}
			printf("%d %d %d\n",a,b,c);
		}

	}
	return 0;
}