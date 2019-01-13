//
//  main.cpp
//  test
//
//  Created by Worlder on 2019/1/13.
//  Copyright © 2019 Worlder. All rights reserved.
//

#include <iostream>
using namespace std;
class Person
{
public:
    Person()
    {
        name = new char[16];
        cout << "Person构造" << endl;
    }
    virtual ~Person()
    {
        delete[] name;
        cout << "Person析构" << endl;
    }
    
private:
    char *name;
};
class Teacher : virtual public Person
{
public:
    Teacher() { cout << "Teacher构造" << endl; }
    ~Teacher() { cout << "Teacher析构" << endl; }
};
class Student : virtual public Person
{
public:
    Student() { cout << "Student构造" << endl; }
    ~Student() { cout << "Student析构" << endl; }
};
class TS : public Teacher, public Student
{
public:
    TS() { cout << "TS构造" << endl; }
    ~TS() { cout << "TS析构" << endl; }
};
int main(int argc, char *argv[])
{
    Person *p = new TS();
    delete p;
    return 0;
}


