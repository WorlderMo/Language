#include "Plane.h"

char PlaneBack[BACK_x][BACK_y] = {  1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
									1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
									1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
									1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
									1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
									1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
									1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
									1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
									1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
									1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
									1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
									1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
									1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
									1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
									1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
									1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
									1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
									1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
									1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
									1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
                                 };

//兼容性背景
char strBackTemp[BACK_x][BACK_y * 2 + 2];

int hero_X = 17;
int hero_Y = 10;
//开始界面
void FengMian()
{
	printf("\n\n\n\t\t\t\t\t\t 《欢迎来到飞机大战》\n");
	printf("\n\t\t\t\t\t         《本游戏由陈子诺赞助开发》\n");
	printf("\n\t\t\t\t\t《W A S D, 控制飞行方向, 空格键开炮》\n");
	printf("\n\t\t\t\t\t          《按任意键继续》\n");
}

//打印背景
void PrintBack1()
{
	int i, j;

	//兼容性背景
	char strBackTemp[BACK_x][BACK_y * 2 + 2] = { 0 };

	//设置英雄位置
	SetHeroPos();
	//装背景
	for (i = 0; i < BACK_x; i++)
	{
		for (j = 0; j < BACK_y; j++)
		{
			switch (PlaneBack[i][j])
			{
			case 0:
				strcat(strBackTemp[i], "  ");
				break;
			case 1:
				strcat(strBackTemp[i], "■");
				break;
			case 2:
				strcat(strBackTemp[i], "士");
				break;
			case 3:
				break;
			}
		}
		strcat(strBackTemp[i], "\n");
	}

    //打印背景
	for (i = 0; i < BACK_x; i++)
	{
		printf(strBackTemp[i]);
	}
}

//设置鼠标位置
void Gotoxy(int x, int y)
{
	COORD rd;
	rd.Y = x;
	rd.X = y * 2;
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), rd);
}
void PrintBack()
{
	int i, j;
	//设置英雄位置
	SetHeroPos();

	//装背景
	for (i = 1; i < BACK_x - 1; i++)
	{
		for (j = 1; j < BACK_y - 1; j++)
		{
			Gotoxy(i, j);
			switch (PlaneBack[i][j])
			{
			case 0:
				/*printf("  ");*/
				break;
			case 1:
				/*printf("■");*/
				break;
			case 2:
				printf("士");
				break;
			case 3:
				break;
			}
		}
	}

}
//设置英雄的位置
void SetHeroPos()
{
	PlaneBack[hero_X][hero_Y] = 2;
}

//控制英雄移动
void HeroPlay()
{
	Gotoxy(hero_X, hero_Y);
	if (GetAsyncKeyState('W') && hero_X > 1)
	{
		PlaneBack[hero_X][hero_Y] = 0;
		printf("  ");
		hero_X--;
		
	}
	else if (GetAsyncKeyState('S') && hero_X < BACK_x - 2)
	{
		PlaneBack[hero_X][hero_Y] = 0;
		printf("  ");
		hero_X++;
		
	}
	if (GetAsyncKeyState('A') && hero_Y > 1)
	{
		PlaneBack[hero_X][hero_Y] = 0;
		printf("  ");
		hero_Y--;
		
	}
	
	else if (GetAsyncKeyState('D') && hero_Y < BACK_y - 2)
	{
		PlaneBack[hero_X][hero_Y] = 0;
		printf("  ");
		hero_Y++;
		
	}
	if (GetAsyncKeyState( VK_SPACE ))
	{
		//printf("0");
	}
}