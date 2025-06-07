/*2. Even or Odd

Task: Ask the user to input an integer. Print whether the number is even or odd using the modulus operator (%).
Concepts: conditionals, input/output, modulo

*/

#include <stdio.h>
#include <stdbool.h>

int check(int number){
    if (number % 2 == 0){
        return true;
    }
    else{
        return false;
    }
}

int main(){
    int number;
    scanf("%d", &number);
    if (check(number) == 1){
        printf("%d is even\n", number);
    }
    else{
        printf("%d is odd\n", number);    
    }
}