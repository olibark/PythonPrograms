/*
1. Temperature Converter

Task: Write a program that asks the user to enter a temperature in Celsius and converts it to Fahrenheit.
Formula: F = C * 9/5 + 32*/


#include <stdio.h>

float convert(float celsius){
    float fahrenheit;
    fahrenheit = (celsius * (9.0 / 5.0)) + 32.0;
    return fahrenheit;
}

int main(){
    float celsius;
    printf("Enter temp in C: ");
    scanf("%f", &celsius);
    float fahrenheit = convert(celsius);
    printf("Temp in F = %.2f\n", fahrenheit);
}