#include <stdio.h>
#include <algorithm>
#define N 100000

using namespace std;

struct stu
{
    int time, level;
} task[N + 10], machine[N + 10];

int cmp(struct stu a, struct stu b)
{
    if (a.time == b.time)
        return a.level > b.level;
    return a.time > b.time;
}
int main()
{
    int n, m;
    while (scanf("%d%d", &n, &m) != EOF)
    {
        for (int i = 1; i <= n; i++)
            scanf("%d%d", &machine[i].time, &machine[i].level);
        for (int i = 1; i <= m; i++)
            scanf("%d%d", &task[i].time, &task[i].level);
        sort(machine + 1, machine + 1 + n, cmp);
        sort(task + 1, task + 1 + m, cmp);
        int j = 1, cnt[105] = {0}, maxm = 0;
        long long ans = 0;
        for (int i = 1; i <= m; i++)
        {
            while (j <= n && task[i].time <= machine[j].time)
            {
                cnt[machine[j].level]++;
                j++;
            }
            for (int k = task[i].level; k <= 100; k++)
            {
                if (cnt[k])
                {
                    maxm++;
                    ans += task[i].time * 200 + task[i].level * 3;
                    cnt[k]--;
                    break;
                }
            }
        }
        printf("%d %d\n", maxm, ans);
    }
    return 0;
}
