#include <stdio.h>
int main(int argc, char const *argv[])
{
	int i;
	while(scanf("%d",&i)!=EOF)
	{
		if(i>89&&i<101)
			printf("A\n");
		else if(i>79&&i<90)
			printf("B\n");
		else if(i>69&&i<80)
			printf("C\n");
		else if(i>59&&i<70)
			printf("D\n");
		else if(i>=0&&i<60)
			printf("E\n");
		else 
			printf("Score is error!\n");
	}
	return 0;
}