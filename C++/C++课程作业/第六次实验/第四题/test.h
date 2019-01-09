//
//  test.h
//  three6
//
//  Created by Worlder on 2018/12/31.
//  Copyright © 2018 Worlder. All rights reserved.
//

#ifndef test_h
#define test_h

#include <string>
#include <algorithm>
using namespace std;

struct node
{
    
    node *next, *prior;
    string data;
    node()
    {
        next = 0;
        prior = 0;
    }
    node(const string &t)
    {
        data = t;
        next = 0;
        prior = 0;
    }
};

class String_list
{
public:
    class iterator
    {
    public:
        iterator(){};
        iterator(node *n) { p = n; };
        iterator(const iterator &i) { p = i.p; };
        
        iterator &operator=(const iterator &rhs)
        {
            if (this != &rhs)
            {
                p = rhs.p;
                return *this;
            }
            else{
                return *this;
            }
        }
        bool operator!=(const iterator &rhs)
        {
            return p != rhs.p;
        }
        
        iterator &operator++() //前置++运算
        {
            p = p->next;
            return *this;
        }
        
        iterator &operator++(int i) //后置++运算
        {
            iterator temp = *this;
            p = p->next;
            return temp;
        }
        
        iterator &operator--() //前置--运算
        {
            p = p->prior;
            return *this;
        }
        
        iterator &operator--(int i) //后置--运算
        {
            iterator temp = *this;
            p = p->prior;
            return temp;
        }
        string &operator*() { return p->data; }
        
    private:
        node *p;
    };
    String_list();  //默认的构造函数
    ~String_list(); //析构函数
    void push_back(const string &t);
    node *begin() { return head->next; }
    node *end() { return head; }
    
private:
    node *head, *limit;
    int num;
    
    node *creat(const string &);
    void uncreat();
    void destroy(node *p);
};

String_list::String_list() : num(0) //默认构造函数 构造只含头结点的空表
{
    node *p = creat("");
    p->next = p->prior = p;
    head = limit = p;
}

node *String_list::creat(const string &t) //为链表开辟新的空间
{
    node *p = new node(t);
    return p;
}

String_list::~String_list() //析构函数
{
    uncreat();
    destroy(head);
}

void String_list::uncreat()
{
    node *temp, *begin;
    begin = head->next;
    while (begin != limit)
    {
        temp = begin->next;
        destroy(begin);
        begin = temp;
    }
    num = 0;
}
void String_list::destroy(node *p)
{
    if (p)
        delete p;
}

void String_list::push_back(const string &t)
{
    node *p = creat(t);
    //尾插法建立双向链表
    head->prior->next = p;
    p->prior = head->prior;
    head->prior = p;
    p->next = head;
    ++num;
}
#endif /* test_h */
