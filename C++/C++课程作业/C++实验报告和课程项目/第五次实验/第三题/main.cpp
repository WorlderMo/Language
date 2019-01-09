//
//  main.cpp
//  three5
//
//  Created by Worlder on 2018/12/31.
//  Copyright © 2018 Worlder. All rights reserved.
//

#include <map>
#include <iostream>
#include <string>
#include <vector>

#include "urls.hpp"
using namespace std;

map<string, vector<int>> xref(istream &in)
{
    string s;
    int line_number = 0;
    map<string, vector<int>> ret;
    
    while (getline(in, s))
    {
        ++line_number;
        
        vector<string> urls = find_urls(s);
        
        // remember that each word occurs on the current line
        for (vector<string>::const_iterator it = urls.begin();
             it != urls.end(); ++it)
            if (find(ret[*it].begin(), ret[*it].end(), line_number) == ret[*it].end())
                ret[*it].push_back(line_number);
    }
    return ret;
}

int main()
{
    // call `xref' using `split' by default
    map<string, vector<int>> ret = xref(cin);
    
    // write the results
    for (map<string, vector<int>>::const_iterator it = ret.begin();
         it != ret.end(); ++it)
    {
        // write the word
        cout << it->first << " occurs on line(s): ";
        
        // followed by one or more line numbers
        vector<int>::const_iterator line_it = it->second.begin();
        cout << *line_it; // write the first line number
        
        ++line_it;
        // write the rest of the line numbers, if any
        while (line_it != it->second.end())
        {
            cout << ", " << *line_it;
            ++line_it;
        }
        // write a new line to separate each word from the next
        cout << endl;
    }
    
    return 0;
}

