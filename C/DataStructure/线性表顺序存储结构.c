#include <stdio.h>

#define MAXSIZE 200  //存储空间初始分配量
#define OK 1
#define ERROR 0
typedef int ElemType;
typedef int Status;  //Status是函数的类型，其值是函数结果的状态代码，如OK等
typedef struct  //定义线性表结构体
{
    ElemType data[MAXSIZE];  //数组存储数据元素，最大值为MAXSIZE
    int length;  //线性表的长度
}SqList;
Status SetList(SqList *L)  //让用户自己建立一个线性表
{
    printf("请输入你的线性表的长度\n");
    scanf("%d", &L->length);
    printf("请输入你的线性表\n");
    for(int i = 0; i < L->length; i++)
    {
        scanf("%d", &L->data[i]);
    }
    printf("恭喜你，你已经成功建立了你的线性表\n");
    return OK;
}
Status GetElem(SqList L, int i )  //获得元素操作
{
    int e;
    if(L.length == 0 || i > L.length)
        return ERROR;
    e = L.data[i-1];
    printf("你获得的元素是：%d\n", e);
    return OK;
}
Status ListInsert(SqList *L, int i, ElemType e)  //插入元素操作
{
    int k;
    if(L->length == MAXSIZE)  //顺序线性表已满
        return ERROR;
    if(i < 1 || i > L->length)  //当i不在范围内
        return ERROR;
    if(i <= L->length)  //若插入的数据位置不在表尾
    {
        for(k = L->length; k >= i - 1; k--)  //将要插入的位置后数据元素向后移动一位
            L->data[k+1] = L->data[k];
    }
    L->data[i-1] = e;  //将新元素插入
    L->length++;
    printf("恭喜你，你已经插入了元素 %d\n", e);
    printf("现在你的线性表是这样的：\n");
    for(int j = 0; j < L->length; j++)
    {
        printf("%d", L->data[j]);
        printf(j == L->length-1 ? "\n" : " ");
    }
    return OK;
}
Status ListDelete(SqList *L, int i)  //删除元素操作
{
    int e, k;
    if(L->length == 0)  //线性表为空
        return ERROR;
    if(i < 1 || i > L->length)  //删除位置不正确
        return ERROR;
    e = L->data[i-1];
    if(i < L->length)  //如果删除的不是最后的位置
    {
        for(k = i; k < L->length; k++)  //将删除位置后续元素前移
            L->data[i-1] = L->data[i];
    }
    L->length--;
    printf("恭喜你，你已经删除了元素 %d\n", e);
    printf("现在你的线性表是这样的：\n");
    for(int j = 0; j < L->length; j++)
    {
        printf("%d", L->data[j]);
        printf(j == L->length-1 ? "\n" : " ");
    }
    return OK;
    return OK;
}
int main(int argc, char const *argv[])
{
    int i, j, e, k;
    SqList L;
    SetList(&L);
    printf("请输入你要获得的元素的位置：\n");
    scanf("%d", &i);
    GetElem(L, i);
    printf("请输入你要插入元素的位置：\n");
    scanf("%d", &j);
    printf("请输入你要插入的元素数据：\n");
    scanf("%d", &e);
    ListInsert(&L, j, e);
    printf("请输入你要删除的元素的位置：\n");
    scanf("%d", &k);
    ListDelete(&L, k);
    return 0;
}
