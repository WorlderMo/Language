#include <stdio.h>
#include <stdlib.h>

#define OK 1
#define ERROR 0
typedef int ElemType;
typedef int Status; //Status是函数的类型，其值是函数结果的状态代码，如OK等
typedef struct Node
{
    ElemType data;
    struct Node *next;
} Node;
typedef struct Node *LinkList; //定义LinkList
Status SetList(LinkList *L)
{
    LinkList cur, pre, head, p;
    int n;
    printf("请输入链表的长度:\n");
    scanf("%d", &n);
    cur = *L = (struct Node *)malloc(sizeof(Node)); //开辟一个新的空间给头结点
    printf("请输入链表数据：\n");
    cur = *L; //pre为指向尾部的结点
    scanf("%d", &cur->data);
    head = cur;
    for (int i = 1; i < n; i++)
    {
        pre = cur;                          //将新生成的结点作为下一个结点的前一个结点
        cur = (Node *)malloc(sizeof(Node)); //生成新结点
        scanf("%d", &cur->data);
        pre->next = cur; //当新生成的结点赋值给前一个结点的next
    }
    cur->next = NULL;
    printf("现在的链表是这样的：\n");
    for (cur = head; cur; pre = cur, cur = cur->next)
        printf("%d ", cur->data);
    printf("\n");
    return OK;
}
Status GetElem(LinkList L) //获得元素操作
{
    int i, j;
    ElemType e;
    LinkList p;
    printf("请输入你要获得元素的下标：\n");
    scanf("%d", &i);
    p = L->next;       //让p指向链表L的第一个结点
    j = 1;             //j为计时器
    while (p && j < i) //p不为空而且计时器j还没有等于i时，循环继续
    {
        p = p->next; //让p指向下一个结点
        j++;
    }
    if (!p || j > i)
        return ERROR; //第i个结点不存在
    e = p->data;
    printf("恭喜你，你获得的第%d个元素为：%d\n", i + 1, e);
    return OK;
}
Status ListInsert(LinkList *L) //插入元素操作
{
    int i, j;
    ElemType e;
    LinkList p, s;
    printf("请输入你要插入元素的下标：\n");
    scanf("%d", &i);
    printf("请输入你要插入的元素数据：\n");
    scanf("%d", &e);
    p = *L; //把链表的第一个结点赋值给p
    j = 1;
    while (p && j < i) //寻找第i-1个结点,
    {
        p = p->next;
        ++j;
    }
    if (!p || j > i)
        return ERROR;
    s = (LinkList)malloc(sizeof(Node)); //生成新的结点
    s->data = e;
    s->next = p->next; //将p的后续结点赋值给s的后续
    p->next = s;       //将s赋值给p的后续
    printf("恭喜你，插入数据成功\n");
    p = *L;
    printf("现在的链表是这样的：\n");
    while (p)
    {
        printf("%d ", p->data);
        p = p->next;
    }
    printf("\n");
    return OK;
}
Status ListDelete(LinkList *L) //删除元素操作
{
    int i, j;
    ElemType e;
    LinkList p, q;
    p = *L;
    j = 1;
    printf("请输入你要删除的元素的下标：\n");
    scanf("%d", &i);
    while (p->next && j < i) //遍历寻找第i-1个结点
    {
        p = p->next;
        ++j;
    }
    if (!(p->next) || j > i)
        return ERROR; //第i个结点不存在
    q = p->next;
    p->next = q->next; //将q的后续赋值给p的后续
    e = q->data;
    printf("你所删除的元素为：%d\n", e);
    free(q);
    p = *L;
    printf("恭喜你，删除数据成功\n");
    printf("现在的链表是这样的：\n");
    while (p)
    {
        printf("%d ", p->data);
        p = p->next;
    }
    printf("\n");
    return OK;
}
int main(int argc, char const *argv[])
{
    LinkList L;
    SetList(&L);
    GetElem(L);
    ListInsert(&L);
    ListDelete(&L);
    return 0;
}
