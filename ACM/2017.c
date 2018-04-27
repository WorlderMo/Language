#include <stdio.h>
int main(int argc, char const *argv[])
{
	int n,k;
	char c;
	scanf("%d",&n);
	getchar();
	for (int i = 0; i < n; i++)
		{
			k = 0;
			while((c=getchar())!='\n')
			{
				if (c>='0'&&c<='9')
				{
					k++;
				}
			}
			printf("%d\n",k );
		}
	return 0;
}