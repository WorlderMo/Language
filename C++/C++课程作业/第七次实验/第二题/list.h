//
//  list.h
//  two7
//
//  Created by Worlder on 2018/12/31.
//  Copyright © 2018 Worlder. All rights reserved.
//

#ifndef list_h
#define list_h

template <class T>
struct node
{
    node<T> *next;
    T number;
};

template <class T>
class Lst
{
public:
    class iterator
    {
    public:
        iterator() {}
        iterator(node<T> *n) { p = n; }
        iterator(const iterator &i) { p = i.p; }
        
        iterator &operator=(const iterator &rhs)
        {
            if (this != &rhs)
            {
                p = rhs.p;
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
        T &operator*() { return p->number; }
        
    private:
        node<T> *p;
    };
    
    Lst() { create(); }
    Lst(const Lst &l) { create(l.data, l.avail); }
    Lst &operator=(const Lst &l);
    ~Lst() { uncreate(); }
    
    iterator begin()
    {
        data = data->next;
        return data;
    }
    const node<T> *begin() const
    {
        data = data->next;
        return data;
    }
    iterator end() { return avail->next; }
    const node<T> *end() const { return avail->next; }
    
    bool empty() const { return data == avail; }
    size_t size() const { return avail - data; }
    
    void push_back(const T &t);
    
private:
    node<T> *data;
    node<T> *avail;
    int num;
    
    void create();
    void create(node<T> *i, node<T> *j);
    void uncreate();
};

template <class T>
void Lst<T>::create()
{
    data = avail = new node<T>;
    
    data->number = 0;
    data->next = nullptr;
    avail->number = 0;
    avail->next = nullptr;
    num = 0;
}
template <class T>
void Lst<T>::create(node<T> *i, node<T> *j)
{
    data = i;
    node<T> *t = i;
    while (t != j)
    {
        t->number = i->number;
        t->next = i->next;
        t = t->next;
        ++num;
    }
    avail = t;
}

template <class T>
Lst<T> &Lst<T>::operator=(const Lst<T> &l)
{
    if (this != &l) //避免自我复制
    {
        uncreate();
        create(l.data, l.avail);
    }
    return *this;
}
template <class T>
void Lst<T>::push_back(const T &t)
{
    node<T> *p = new node<T>;
    p->number = t;
    p->next = nullptr;
    avail->next = p;
    avail = p;
    
    ++num;
}
template <class T>
void Lst<T>::uncreate()
{
    if (data)
    {
        node<T> *it = data;
        while (it != avail)
        {
            node<T> *tnext = it->next;
            delete it;
            it = tnext;
        }
        avail = data = 0;
        num = 0;
    }
}

#endif /* list_h */
