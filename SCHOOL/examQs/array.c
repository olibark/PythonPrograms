#include <stdio.h>
#include <math.h>
int main() {
    int times;
    printf("How many num: ");
    scanf("%d", &times);
    float numbers[times];
    float number, total = 0;
    for (int i = 0; i < times; i++){
        printf("Number: ");
        scanf("%f", &numbers[i]);
    }
    for (int i = 0; i < times; i++){
        total += numbers[i];
        printf("%.2f\n", numbers[i]);
    }
    printf("Average: %.2f\n", total / times);
}