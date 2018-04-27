#include <stdio.h>
#include <stdlib.h>
typedef int ElemType;
typedef struct BiTNode
{
    ElemType data;
	struct BiTNode *lchild, *rchild;
}BiTNode, *BiTree;
int Delete(BiTree *p);
int SearchASD(BiTree T, ElemType key, BiTree f, BiTree *p)
{
	if (!T)
	{
		*p = f;
		return 0;
	}
	else
	{
		if (key == T->data)
		{
			*p = T;
			return 1;
		}
		else
		{
			if (key < T->data)
			{
				return SearchASD(T->lchild, key, T, p);
			}
			else
			{
				return SearchASD(T->rchild, key, T, p);
			}
		}
	}
}
int InsertASD(BiTree *T, ElemType key)
{
	BiTree p, s;
	if (!SearchASD(*T, key, NULL, &p))
	{
		s = (BiTree)malloc(sizeof(BiTNode));
		s->data = key;
		s->lchild = s->rchild = NULL;
		if (!p)
		{
			*T = s;
		}
		else
		{
			if (key < p->data)
			{
				p->lchild = s;
			}
			else
			{
				p->rchild = s;
			}
		}
		return 1;
	}
	else
	{
		return 0;
	}

}
void ProOrderTraverse(BiTree T)
{
	if (T == NULL)
	{
		return;
	}
	else
	{
		printf("%d ", T->data);
		ProOrderTraverse(T->lchild);
		//printf("%d ",T->data);
		ProOrderTraverse(T->rchild);
	}
}

void MidOrderTraverse(BiTree T)
{
	if (T == NULL)
	{
		return;
	}
	else
	{
		//printf("%d ",T->data);
		MidOrderTraverse(T->lchild);
		printf("%d ", T->data);
		MidOrderTraverse(T->rchild);
	}
}

int DeleteASD(BiTree *T, ElemType key)
{
	if (!*T)
	{
		return 0;
	}
	else
	{
		if (key == (*T)->data)
		{
			return Delete(T);
		}
		else
		{
			if (key < (*T)->data)
			{
				return DeleteASD(&(*T)->lchild, key);
			}
			else
			{
				return DeleteASD(&(*T)->rchild, key);
			}
		}
	}
}
int Delete(BiTree *p)
{
	BiTree q, s;
	if ((*p)->rchild == NULL)
	{
		q = *p;
		*p = (*p)->lchild;
		free(q);
	}
	else
	{
		if ((*p)->lchild == NULL)
		{
			q = *p;
			*p = (*p)->rchild;
			free(q);
		}
		else
		{
			q = *p;
			s = (*p)->lchild;
			while (s->rchild)
			{
				q = s;
				s = s->rchild;
			}
			(*p)->data = s->data;
			if (q != *p)
			{
				q->rchild = s->lchild;
			}
			else
			{
				q->lchild = s->lchild;
			}
			free(s);
		}
	}
	return 1;
}



int main()
{
	int i;
	int a[10] = { 62,88,58,47,35,73,51,99,37,93 };
	BiTree T = NULL;
	for (i = 0; i<10; i++)
	{
		InsertASD(&T, a[i]);
	}
	printf("first:\n");
	ProOrderTraverse(T); printf("\n");
	MidOrderTraverse(T); printf("\n");

	printf("insert 95\n");
	InsertASD(&T, 95);
	ProOrderTraverse(T); printf("\n");
	MidOrderTraverse(T); printf("\n");

	printf("delete 51\n");
	DeleteASD(&T, 51);
	ProOrderTraverse(T); printf("\n");
	MidOrderTraverse(T); printf("\n");
	getchar();
	return 0;
}
