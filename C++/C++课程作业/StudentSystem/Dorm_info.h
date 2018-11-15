//
// Created by Worlder on 2018/11/1.
//

#ifndef STUDENTSYSTEM_DORM_INFO_H
#define STUDENTSYSTEM_DORM_INFO_H


#include <vector>
#include <fstream>
#include <string>

//using std::string;
//using std::vector;
//using std::ifstream;
using namespace std;

struct Dorm_room {
    vector<string> roomStudent;
    int bedNum;
};

struct Dorm_floor {
    vector<Dorm_room> room;
    int roomNum;
};

struct Dorm_info {
    vector<Dorm_floor> floor;
    int floorNum;
};

void readAddDorm(ifstream &is, Dorm_info &dorm);

void readAddDorm_new(ifstream &is, Dorm_info &dorm);

#endif //STUDENTSYSTEM_DORM_INFO_H
