#include"output.h"
#include<iostream>
#include<string>
#include<map>
#include<algorithm>
using namespace std;

void sortofvalue(map<string, massage>m, vector<pair<string, massage> >& v) {

	for (map<string, massage>::iterator it = m.begin(); it != m.end(); ++it)
		v.push_back(make_pair(it->first, it->second));
	sort(v.begin(), v.end(), [](const pair<string, massage>& x,
		const pair<string, massage>& y) {
		return x.first > y.first;
	});
	sort(v.begin(), v.end(), [](const pair<string, massage>& x,
		const pair<string, massage>& y) {
		return x.second.time < y.second.time;
	});
	return;
}

void output(map<string, massage>& counters)
{
	vector<pair<string, massage> >vect;
	sortofvalue(counters, vect);
	for (vector<pair<string, massage> >::iterator it = vect.begin();
		it != vect.end(); ++it) {
        cout << it->first << ": " << it->second.time << " times, line number: ";

		vector<int>::const_iterator line_it = it->second.position.begin();
		cout << *line_it;
		++line_it;
		while (line_it != it->second.position.end()) {
			cout << ", " << *line_it;
			++line_it;
		}
		cout << endl;
	}
}
