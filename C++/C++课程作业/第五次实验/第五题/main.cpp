//
//  main.cpp
//  four5
//
//  Created by Worlder on 2018/12/31.
//  Copyright © 2018 Worlder. All rights reserved.
//

#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <map>
#include <stdexcept>
#include <string>
#include <vector>
#include <iterator>
#include <list>
#include <time.h>
#include "split.hpp"


using namespace std;

typedef vector<string> Rule;
typedef vector<Rule> Rule_collection;
typedef map<string, Rule_collection> Grammar;

// read a grammar from a given input stream
Grammar read_grammar(istream& in)
{
    Grammar ret;
    string line;
    
    // read the input
    while (getline(in, line)) {
        
        // `split' the input into words
        vector<string> entry = split(line);
        
        if (!entry.empty())
            // use the category to store the associated rule
            ret[entry[0]].push_back(
                                    Rule(entry.begin() + 1, entry.end()));
    }
    return ret;
}
template<typename out>
void gen_aux(const Grammar&, const string&, out*);

int nrand(int);

template<typename out>
void gen_sentence(const Grammar& g, out os)
{
    gen_aux(g, "<sentence>", &os);
}

bool bracketed(const string& s)
{
    return s.size() > 1 && s[0] == '<' && s[s.size() - 1] == '>';
}

template<typename out>
void gen_aux(const Grammar& g, const string& word, out* ret)
{
    
    if (!bracketed(word)) {
        (**ret) = word;
        (*ret)++;
    }
    else {
        // locate the rule that corresponds to `word'
        Grammar::const_iterator it = g.find(word);
        if (it == g.end())
            throw logic_error("empty rule");
        
        // fetch the set of possible rules
        const Rule_collection& c = it->second;
        
        // from which we select one at random
        const Rule& r = c[nrand(c.size())];
        
        // recursively expand the selected rule
        for (Rule::const_iterator i = r.begin(); i != r.end(); ++i)
            gen_aux(g, *i, ret);
    }
}

int main()
{
    // generate the sentence
    
    list<string> sentence;
    gen_sentence(read_grammar(cin), back_inserter(sentence));
    // write the first word, if any
    list<string>::const_iterator it = sentence.begin();
    if (!sentence.empty()) {
        cout << *it;
        ++it;
    }
    
    // write the rest of the words, each preceded by a space
    while (it != sentence.end()) {
        cout << " " << *it;
        ++it;
    }
    
    cout << endl;
    return 0;
}

// return a random integer in the range `[0,' `n)'
int nrand(int n)
{
    if (n <= 0 || n > RAND_MAX)
        throw domain_error("Argument to nrand is out of range");
    const int bucket_size = RAND_MAX / n;
    int r;
    
    srand((unsigned)time(NULL));
    
    //cout << rand() << endl;
    do
        r = (rand()) / bucket_size;
    while (r >= n);
    //cout << rand() << endl;
    //r = (rand()) % n;
    return r;
}
