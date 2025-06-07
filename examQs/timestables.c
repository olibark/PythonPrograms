#include <stdio.h>

int main() {
    for (int i = 1; i < 40001; i ++) {
        for (int j = 1; j < 21; j++) {
            int a = i * j;
            printf("%d x %d = %d\n", i, j, a);
        }
        printf("%d times tables\n", i);
    }
}