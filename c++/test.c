#include "stdafx.h"
#include "stdlib.h"

void func1(void) { printf("1\n"); };
void func2(void) { printf("2\n"); };
void func3(void) { printf("3\n"); };
void func4(void) { printf("4\n"); };
void func5(void) { printf("5\n"); };

int main()
{
    int n;
    while (1)
    {
        printf("input:");
        scanf_s("%d", &n);
        void(*fptr[5])(void);
        fptr[0] = func1;
        fptr[1] = func2;
        fptr[2] = func3;
        fptr[3] = func4;
        fptr[4] = func5;
        if (n > 5)
            break;
        fptr[(n-1)]();
    }
    printf("finish");
    system("pause");
    return 0;
}
 