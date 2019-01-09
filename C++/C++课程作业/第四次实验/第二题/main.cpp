//
//  main.cpp
//  test
//
//  Created by Worlder on 2018/12/30.
//  Copyright © 2018 Worlder. All rights reserved.
//

#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

string target = "";

void cat(string s) {
    target += s;
}

int main() {
    vector<string> words = vector<string>(3, "mohailang");
    for_each(words.begin(), words.end(), cat);
    cout << target << endl;
    
    return 0;
}

