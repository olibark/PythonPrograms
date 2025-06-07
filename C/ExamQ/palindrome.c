#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

// Helper function to preprocess the string
void preprocessString(char* str, char* cleaned) {
    int j = 0;
    for (int i = 0; str[i] != '\0'; i++) {
        if (isalnum(str[i])) { // Keep only alphanumeric characters
            cleaned[j++] = tolower(str[i]);
        }
    }
    cleaned[j] = '\0'; // Null-terminate the cleaned string
}

bool isPalindrome(char str[]) {
    char cleaned[1000]; // Assuming the input string won't exceed 1000 characters
    preprocessString(str, cleaned);

    int len = strlen(cleaned);
    for (int i = 0; i < len / 2; i++) {
        if (cleaned[i] != cleaned[len - i - 1]) {
            return false;
        }
    }
    return true;
}

int main() {
    char str[1000];
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);

    // Remove the newline character from fgets
    str[strcspn(str, "\n")] = '\0';

    if (isPalindrome(str)) {
        printf("The string is a palindrome.\n");
    } else {
        printf("The string is not a palindrome.\n");
    }

    return 0;
}