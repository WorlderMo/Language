#include <stdio.h>

#define MAXSIZE 200
#define OK 1
typedef int SElemType;  //SElemType类型根据实际情况而定，这里假设int
typedef struct
{
    SElemType data[MAXSIZE];
    int top;  //用于栈顶指针
}SqStack;

int Push( SqStack *s, SElemType e )
{
    if ( s->top == MAXSIZE - 1 )  //栈满
    {
        return 0;
    }
    s->top++;  //栈顶指针+1
    s->data[s->top] = e;  //将新插入元素赋值给栈顶空间
    return 1;
}
int Pop( SqStack *s, SElemType *e)
{
    if ( s->top == -1 )
        return 0;
    *e = s->data[s->top];  //将要删除的栈顶元素赋值给e
    s->top--;  //栈顶指针-1
    return 1;
}
