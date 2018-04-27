#ifndef _PLANE   //#pragma once
#define _PLANE
#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <Windows.h>
#include <time.h>


//背景大小
#define  BACK_X   20
#define  BACK_Y   20

struct _Node
{
	int y;
	int x;
	struct _Node* pNext;
};
typedef int bool;
#define true  1
#define false 0
//封面
void FengMian();
//打印
void PrintfBack();
//设置英雄的位置
void SetHeroPos();
//控制英雄移动
void HeroPlay(); //GetAsyncKeyState
//打印
void PrintfBack1();
//设置鼠标位置
void GotoXY(int x, int y);
//产生飞机
void ReducePlane();
//飞机下落
void PlaneDown();
//子弹链表尾添加
void InsertDan(int y, int x);
//子弹动起来
void DanRun();
//显示子弹
void ShowDan();
//消除子弹
void DeleteDan();
//飞机碰撞
void DeletePlane();
//删除链表指定的节点
void DeleteNode(struct _Node* p);
//计分
void Score();
//计分
bool IsHeroDie1();


#endif