#include <stdio.h>
#include <stdlib.h>

typedef char VertexType;
typedef int EdgeType;
typedef int Boolean;//Boolean是布尔类型，其值是TRUE和FALSE
#define MAXVEX 10//最大顶点数
Boolean visited[MAXVEX];//访问标志的数组
#define TRUE 1
#define FALSE 0
typedef struct
{
	VertexType Vexs[MAXVEX];//顶点表
	EdgeType arc[MAXVEX][MAXVEX];//邻接矩阵
	int numVertexes;//图中当前的顶点
}MGraph;

void CreateMGraph(MGraph *G) //建立一个无向图
{
	int i, j,  k, w;
	printf("请输入顶点数\n");
	scanf("%d", &G->numVertexes);//输入顶点数
	printf("请输入相应数目的顶点信息，以建立顶点表\n");
	fflush(stdin);
	for (i = 0; i < G->numVertexes; ++i)//读入顶点信息，建立顶点表
	{
		printf("顶点%d: ",i+1);
		scanf("%c", &G->Vexs[i]);
		fflush(stdin);
	}
	for (i = 0; i < G->numVertexes; i++)//初始化边表
	{
		for (j = 0; j < G->numVertexes; j++)
			G->arc[i][j] = 0;
	}
	printf("请输入邻接矩阵\n");
	for (k = 0; k < G->numVertexes; k++)//读入(vi,vj)信息，建立邻接矩阵
	{
		for(w = 0; w < G->numVertexes; w++)
			scanf("%d", &G->arc[k][w]);
	}
}
void DFS(MGraph G, int i)//邻接矩阵的深度优先递归算法
{
	int j;
	visited[i] = TRUE;
	printf("%C", G.Vexs[i]);//打印顶点，也可以其他操作
	printf(" ");
	for (j = 0; j < G.numVertexes; j++)
		if (G.arc[i][j] == 1 && !visited[j])
			DFS(G, j);//对为访问的邻接顶点递归调用
}
void DFSTraverse(MGraph G)//深度优先遍历
{
	int i;
	for (i = 0; i < G.numVertexes; i++)
		visited[i] = FALSE;//初始化所有顶点状态都是未访问过状态
	for (i = 0; i < G.numVertexes; i++)
		if (!visited[i])//对未访问的顶点调用DFS，若是连通图，只会执行一次
			DFS(G, i);
}
int main()
{
	MGraph G;
	CreateMGraph(&G);
	printf("\n深度遍历:\n");
	DFSTraverse(G);
	return 0;
}
/*
0 0 0 0 1 0 0
0 0 1 1 0 0 0
0 1 0 1 0 0 0
0 1 0 0 1 1 0
1 0 0 1 0 0 1
0 0 0 1 0 0 0
0 0 0 0 1 0 0
*/
