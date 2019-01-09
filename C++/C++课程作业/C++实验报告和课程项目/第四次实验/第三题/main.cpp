#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <algorithm>
#include"split.h"
#include"output.h"
using namespace std;


void match(istream& in, map<string, massage>& counters)
{
	string line;
	int line_number = 0;
	while (getline(in, line)) {
		++line_number;
		vector<string> words = split(line);
		for (auto& w : words)
		{
			counters[w].position.push_back(line_number);
			++counters[w].time;
		}
	}
	return;
}

int main() {
	string s;
	map<string, massage> counters;
    
    match(cin, counters);
	output(counters);
	
	return 0;
}

