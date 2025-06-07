#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

void choices() {
    srand(time(NULL)); // Seed the random number generator with the current time
    while (1) {
        int random_number = rand(); // Generate a random number
        printf("Random number: %d\n", random_number);
        usleep(10000); // Wait for 10 milliseconds (10,000 microseconds)
    }
}

int main() {
    choices();
    return 0;
}