#include <stdio.h>
#include <time.h>
#include <stdlib.h>

void genPass(int lenofpass) {
    const char available[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    const char emily[] = "Emily is an idiot and she stinks of poo";
    char password[lenofpass + 1];  // Allocate extra space for the null terminator
    int half = lenofpass / 2;
    
    for (int i = 0; i < lenofpass; i++) {
        if (i == half) {
            password[i] = emily[0];
        } else {
            int place = rand() % (sizeof(available) - 1);
            password[i] = available[place];
        }
    }
    
    password[lenofpass] = '\0'; // Properly null-terminate the string
    printf("Password is: %s\n", password);
}

int main() {
    int lenofpass;
    printf("Enter password length: ");
    if (scanf("%i", &lenofpass) != 1 || lenofpass <= 0) {
        printf("Invalid input.\n");
        return 1;
    }
    
    srand(time(NULL));  // Seed random generator once
    genPass(lenofpass);
    
    return 0;
}
