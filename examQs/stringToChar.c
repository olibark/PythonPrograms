#include <stdio.h>
#include <string.h>

int main() {
    char string[100];
    scanf("%s", string);
    printf("%s\n", string);
    for (int i = 0; i < strlen(string); i++) {
        printf("%c\n", string[i]);
    }
}