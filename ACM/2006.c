#include <stdio.h>
int main(int argc, char const *argv[])
{
	int n,a[1000];
	while(scanf("%d",&n) != EOF)
	{
		int s = 1;
		for (int i = 0; i < n; i++)
		{
			scanf("%d",&a[i]);
			if(a[i]%2 != 0)
			{
				s = s * a[i];
			}
		}
		printf("%d\n",s);
	}
	return 0;
}