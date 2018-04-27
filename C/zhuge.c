#include <stdio.h>
#define n 5

struct student
{
    int number;
    char name[20];
    double sub[3];
} cla[n];

void input(struct student stu[n]);

int main()
{
    struct student stu[n];
    input(stu);
    return 0;
}
void input(struct student stu[n])
{
    int i, j;
    for (i = 0; i < n; i++)
    {
        scanf("%d", &stu[i].number);
        gets(stu[i].name);
        for (j = 0; j < 3; j++)
            scanf("%lf", &stu[i].sub[j]);
    }
}
