#include <stdio.h>

int main()
{
    char buff[5];
    int feof1, feof2, feof3;
    int count1, count2, count3;
    FILE *fp = fopen("test.txt", "r");
    count1 = fread(buff, 1, 5, fp);
    feof1 = feof(fp);
    count2 = fread(buff, 1, 5, fp);
    feof2 = feof(fp);
    count3 = fread(buff, 1, 5, fp);
    feof3 = feof(fp);
    printf("%d,%d,%d\n", count1, count2, count3);
    printf("%d,%d,%d\n", feof1, feof2, feof3);
    return 0;
}
