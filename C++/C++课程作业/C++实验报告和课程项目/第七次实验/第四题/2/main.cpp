//
//  main.cpp
//  four7-2
//
//  Created by Worlder on 2019/1/1.
//  Copyright © 2019 Worlder. All rights reserved.
//

#include<iostream>
#include"Str.h"
using namespace std;

int main() {
    
    str string("mohailang");
    str string2("520123");
    string.insert(&string[1],&string2[0],&string2[3]);
    cout << "插入后:" << endl;
    cout << string <<endl;
}
