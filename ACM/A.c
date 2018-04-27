#include <stdio.h>


int main(int argc, char const *argv[])
{
	int i;
	int s[100];
	s[0]=7;
	s[1]=11;
	while(scanf("%d",&i)!=EOF)
	{
		if(i<1000000)
		{
			if(i>=2)
			{
				s[i]=s[i-1]+s[i-2];
			}
			if(s[i]%3==0)
			{
				printf("yes\n");
			}
			else
			{
				printf("no\n");
			}
		}
	}
	return 0;
}