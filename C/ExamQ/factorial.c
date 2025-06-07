#include <stdio.h>

int main() {
    long double number, i;
    long double factorial = 1;
    printf("Enter a positive integer: ");
    scanf("%Lf", &number);
    for (i = 1; i <= number; i++){
        factorial *= i;
    }
    printf("Factorial of %Lf = %.0Lf\n", number, factorial);
}