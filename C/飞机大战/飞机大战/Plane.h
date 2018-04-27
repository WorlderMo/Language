#ifndef _PLANE
#define _PLANE

#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <Windows.h>

//背景大小
#define BACK_x 20
#define BACK_y 20

//开始界面
void FengMian();

//打印背景
void PrintBack();

void PrintBack1();

//设置英雄的位置
void SetHeroPos();

//控制英雄移动
void HeroPlay();

//设置鼠标位置
void Gotoxy(int x, int y);

#endif