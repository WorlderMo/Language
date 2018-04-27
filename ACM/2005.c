#include <stdio.h>
int main(int argc, char const *argv[])
{
	int year,moon,day;
	int month[12]={31,28,31,30,31,30,31,30,31,30,31,30};
	int i,sum;
	while(scanf("%d/%d/%d",&year,&moon,&day)!=EOF)
	{
		sum=0;
		for(i=0;i<moon-1;i++)
		{
			sum+=month[i];
		}
		sum+=day;
		if(year%400==0)
		{
			if(moon>2)
				sum+=1;
		}
		printf("%d\n",sum );
	}
	return 0;
}