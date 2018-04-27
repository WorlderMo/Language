#include <stdio.h>
#include <stdlib.h>
#define TRUE 1
#define FALSE 0
typedef char TElemType;
typedef struct BiTNode  //结点结构
{
    char data;  //结点数据
    struct BiTNode *lchild, *rchild;  //左右孩子指针
}BiTNode, *BiTree;

BiTree CreateBitree(BiTree *T) {
    TElemType ch;
    scanf("%c", &ch);
    if (ch == '#')
        *T = NULL;
    else
    {
        *T = (BiTree)malloc(sizeof(BiTNode));
        if (!*T)
            exit (0);
        (*T)->data = ch;  //生成根结点
        CreateBitree (&(*T)->lchild);  //生成左子树
        CreateBitree (&(*T)->rchild);  //生成右子树
    }
    return *T;
}
BiTree SearchBST(BiTree T, TElemType key)
{
    if (!T)  //查找不成功
    {
        printf("查找不成功\n");
        return NULL;
    }
    else if(key == T->data)  //查找成功
    {
        printf("查找成功\n");
        return T;
    }
    else if (key < T->data)
        return SearchBST(T->lchild, key);  //在左子树继续查找
    else
        return SearchBST(T->rchild, key);  //在右子树继续查找
}
void PrintBST( BiTree T )
{
    if( T ) {
        PrintBST( T->lchild );
        printf("%c ", T->data);
        PrintBST( T->rchild );
    }
}
int main(int argc, char const *argv[]) {
    BiTree T;
    TElemType key;
    CreateBitree(&T);
    printf("中序遍历：");
    PrintBST(T);
    printf("\n请输入你要查找的元素：\n");
    fflush(stdin);
    scanf("%c", &key);
    SearchBST(T, key);
    getchar();
    return 0;
}
