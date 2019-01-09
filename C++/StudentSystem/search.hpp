//
//  search.hpp
//  StudentSystem
//
//  Created by Worlder on 2019/1/1.
//  Copyright © 2019 Worlder. All rights reserved.
//

#ifndef search_hpp
#define search_hpp

#include <stdio.h>
#include "Student_new.hpp"

void search_prompt();
void search(vector<Student_new>& vecStudNew, Dorm_info& dorm);
void accordingNameGetRoom(vector<Student_new>& vecStudNew);
void getMaxAndMin_weight(vector<Student_new>& vecStudNew);
void getMaxAndMin_charm(vector<Student_new>& vecStudNew);
void getMaxAndMin_money(vector<Student_new>& vecStudNew);
void getMaxAndMin_knowledge(vector<Student_new>& vecStudNew);
void getLove(vector<Student_new>& vecStudNew);
void accordingRoomGetName(Dorm_info& dorm);
void loveTimesMost(vector<Student_new>& vecStudNew);
void range_weight(vector<Student_new>& vecStudNew);
void range_charm(vector<Student_new>& vecStudNew);
void range_money(vector<Student_new>& vecStudNew);
void range_knowledge(vector<Student_new>& vecStudNew);
void allLoveMost(vector<Student_new>& vecStudNew);


#endif /* search_hpp */
