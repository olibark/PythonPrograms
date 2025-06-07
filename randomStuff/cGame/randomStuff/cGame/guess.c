#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
    srand((unsigned)time(NULL));
    int target = rand() % 100 + 1;
    int guess = 0;
    int attempts = 0;

    printf("Guess a number between 1 and 100\n");

    while (1) {
        printf("Enter guess: ");
        if (scanf("%d", &guess) != 1) {
            printf("Invalid input. Exiting.\n");
            return 1;
        }
        attempts++;
        if (guess < target) {
            printf("Too low!\n");
        } else if (guess > target) {
            printf("Too high!\n");
        } else {
            printf("Correct! You guessed in %d attempts.\n", attempts);
            break;
        }
    }

    return 0;
}