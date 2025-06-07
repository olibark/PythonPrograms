#include <stdio.h>
#include <string.h>
#include <strhash.h>
#define ULL unsigned long long
void hash(input) {
    char *input;
    int i;
    ULL hash = 0;
    int len = strlen(input);
    for (int i = 0; i < len; i++) {
        hash = (hash * 31 + input[i]) % 1000000007;
    }
    printf("Hash value: %llu\n", hash);
}

int main() {
    char input[100];
    scanf("%s", &input);
    hash(input);
    return 0;
}