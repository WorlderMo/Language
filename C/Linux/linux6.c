#include <stdio.h>
#include <unistd.h>

#include <sys/types.h>
#include <sys/wait.h>
int main()
{
    int pid, a, b;
    int status;
    pid = fork();
    if (pid == 0)
    {
        close(0);
        open("test1.txt", 2);
    }
    scanf("%d%d", &a, &b);
    printf("%d\n", a + b);
    if (pid > 0)
        waitpid(pid, &status, 0);
    return 0;
}
