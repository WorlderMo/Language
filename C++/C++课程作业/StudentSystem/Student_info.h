//
// Created by Worlder on 2018/10/25.
//

#ifndef STUDENTSYSTEM_STUDENT_INFO_H
#define STUDENTSYSTEM_STUDENT_INFO_H

#include ""
#include "exprtk.hpp"
#include <string>
#include <vector>
#include <map>

using namespace std;

// 学生生活信息结构体
typedef struct iptData
{
    int FLOOR;
    int ROOM;
    int CAPACITY;
    double WEIGHT;
    double MONEY;
    double KNOWLEDGE;
    double CHARM;
    double FOOD_WEIGHT;
    double FOOD_COST;
    double STUDY_WEIGHT;
    double STUDY_KNOWLEDGE;
    double WORK_MONEY;
    double WORK_WEIGHT;
    double LOVE_STANDARD;
    double LOVE_RECONSTRUCT_STANDARD;

    double HEALTH;
    double LOOKS;
    double EXERCISE_WEIGHT;
    double EXERCISE_HEALTH;
    double MAKEUP_MONEY;
    double MAKEUP_LOOKS;

    string SAVE_FILE_NAME;
    vector<string> iptConfigVecStr;
}iptData;

// 学生个人信息类
class Student_info
{
private:
    string name;
    string sex;

    int floor;
    int room;
    int bed;
    double money;
    double charm;
    double knowledge;
    double weight;


    //todo: 学生生活函数
};


#endif //STUDENTSYSTEM_STUDENT_INFO_H
