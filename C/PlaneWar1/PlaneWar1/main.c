
#include "plane.h"

int main(void)
{
	unsigned int nCount = 0;
	//不显示光标
	CONSOLE_CURSOR_INFO cur_info = {1, 0};
	SetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE), &cur_info);

	//封面
	FengMian();

	//按空格键继续
	_getch();

	//清空控制台
	system("cls");

	//显示背景
	PrintfBack1();

	while (1)
	{
		//子弹动起来
		DanRun();
		//清空控制台
		//system("cls");
		if (0 == nCount % 10)
		{
			//飞机下落
			PlaneDown();
		}

		
		//英雄运动
		HeroPlay();

		//显示背景
		PrintfBack();
		//英雄死亡判断
		if (false == IsHeroDie1())
		{
			break;
		}
		nCount++;
		Sleep(50);
	}
	GotoXY(21, 0);
	printf ("飞机炸了\n");
	system("pause");
	return 0;
}

