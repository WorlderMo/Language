//
//  Dorm_info.hpp
//  StudentSystem
//
//  Created by Worlder on 2019/1/1.
//  Copyright © 2019 Worlder. All rights reserved.
//

#ifndef Dorm_info_hpp
#define Dorm_info_hpp

#include <stdio.h>
#include <vector>
#include <fstream>
#include <string>

using namespace std;

struct Dorm_room
{
    vector<string> roomStudent;
    int bedNum;
};

struct Dorm_floor
{
    vector<Dorm_room> room;
    int roomNum;
};

struct Dorm_info
{
    vector<Dorm_floor> floor;
    int floorNum;
};
void readAddDorm(ifstream &is, Dorm_info &dorm);
void readAddDorm_new(ifstream &is, Dorm_info &dorm);

#endif /* Dorm_info_hpp */
