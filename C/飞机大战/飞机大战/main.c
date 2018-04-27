
#include "Plane.h"

extern char PlaneBack[BACK_x][BACK_y];

int main(void)
{
	//开始界面
	FengMian();
	//按任意键继续
	_getch();

	//清空控制台
	system("cls");

	//打印背景
	PrintBack1();

	while (1)
	{
		//清空控制台
		/*system("cls");*/
		//英雄移动
		HeroPlay();
		//英雄动了就重新打印背景
		PrintBack();

		Sleep(100);
	}
	return 0;
}

