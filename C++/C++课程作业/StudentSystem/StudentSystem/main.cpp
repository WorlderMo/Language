//
//  main.cpp
//  StudentSystem
//
//  Created by Worlder on 2019/1/1.
//  Copyright © 2019 Worlder. All rights reserved.
//

#include "Student_info.hpp"
#include "Student_new.hpp"
#include "Dorm_info.hpp"
#include "search.hpp"
#include <vector>
#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;

iptData configData;
iptData configData_new;

//int main()
int main(int argt, char *argv[])
{
    vector<Student_new> vecStudNew;
    Student_new student;
    Dorm_info dorm;
    ifstream in;
    
    //讀取配置信息
//    Student_new::readConfig(argv[1], configData_new);
    Student_new::readConfig(configData_new);        //为了方便调试而编写的读取config.txt文件的函数，此函数直接打开config.txt，不需要获得参数argv[1]
    cout << "配置信息显示完毕，继续按任意键可进入查询界面" << endl;
    cin.get();
    system("clear");
    
    //宿舍初始化
    dorm.floorNum = configData_new.FLOOR;
    for (int i = 0; i < configData_new.FLOOR; i++)
    {
        Dorm_floor dFloor;
        for (int j = 0; j < configData_new.ROOM; j++)
        {
            Dorm_room dRoom;
            dRoom.bedNum = configData_new.CAPACITY;
            dFloor.room.push_back(dRoom);
        }
        dFloor.roomNum = configData_new.ROOM;
        dorm.floor.push_back(dFloor);
    }
    
    //打开dispatch.txt
//    in.open(argv[2]);
    in.open("/Users/worlder/Documents/Language/C++/StudentSystem/dispatch.txt");        //这是我电脑上dispatch.txt的路径
    if (!in.is_open())
    {
        cout << "Error opening file dispatch.txt" << endl;
        exit(1);
    }
    while (!in.eof())
    {
        if (student.readDorm(in))
        {
            vecStudNew.push_back(student);
        }
    }
    
    Student_new::init(vecStudNew);
    in.close();
    
    //打开instruction.txt
//    in.open(argv[3]);
    in.open("/Users/worlder/Documents/Language/C++/StudentSystem/instructions.txt");        //这是我电脑上instructions.txt的路径
    if (!in.is_open())
    {
        cout << "Error opening file instruction.txt" << endl;
        exit(1);
    }
    while (!in.eof())
    {
        Student_new::readInstruct(in, vecStudNew, dorm); //讀取各種指令
    }
    in.close();
    
    Student_new::putStudentInRoom(vecStudNew, dorm); //將學生“存入”其所屬的房間
    
    //實現各查詢功能
    search(vecStudNew, dorm);
    system("clear");
    cout << "查询完毕，继续按任意键可实现Save功能" << endl;
    cin.get();
    
    //實現Save功能
    Student_new::saveData(vecStudNew, dorm);
    cout << "实现Save功能成功！" << endl;
    cout << "保存完毕，继续按任意键可实现Load功能！" << endl;
    cin.get();
    
    vector<Student_new> vecStudNewLoad;
    Dorm_info dormLoad;
    iptData configLoad;
    //实现Load功能
    Student_new::loadData(vecStudNewLoad, dormLoad, configLoad);
    cout << "实现Load功能成功！" << endl;
    return 0;
}


