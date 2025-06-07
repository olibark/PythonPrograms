#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int createNumber(){
    int number;
    srand(time(NULL));
    number = rand() % 100 + 1;
    return number;
}

int main() {
    int number = createNumber();
    int guess;

    printf("Guess number:");
    scanf("%d", &guess);
    while (guess != number){
        if (guess < number){
            printf("too low!!\n");
        }
        else{
            printf("Too high!!\n");
        }
        scanf("%d", &guess);
    }
}