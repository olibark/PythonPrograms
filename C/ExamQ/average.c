#include <stdio.h>
/*
int main() {
    int noOfValues;
    float sum = 0.0, average;
    printf("Enter number of values: ");
    scanf("%d", &noOfValues);
    int values[noOfValues];
    for (int i = 1; i <= noOfValues; i++) {
        printf("Enter value %d: ", i);
        scanf("%d", &values[i - 1]);
        sum += values[i];
    }
    printf("Sum = %.2f\n", sum);
    average = sum / noOfValues;
    printf("Average = %.2f\n", average);
}
*/

#include <stdio.h>

int main() {
    int noOfValues;
    float sum = 0.0, average;
    printf("Enter number of values: ");
    scanf("%d", &noOfValues);
    int values[noOfValues];
    for (int i = 0; i < noOfValues; i++) {
        printf("Enter value %d: " , i + 1);
        scanf("%d", &values[i]);
        sum += values[i];
    }
    printf("Sum = %.2f\n", sum);
    average = sum / noOfValues;
    printf("Average = %.2f\n", average);
}
