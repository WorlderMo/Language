#ifndef GUARD_OUTPUT
#define GUARD_OUTPUT
#include<vector>
#include<string>
#include<map>
using namespace std;

struct massage {
	int time;
	vector<int> position;
};

void output(map<string, massage>& counters);
#endif 

 
