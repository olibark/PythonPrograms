#include <stdbool.h>
#include <stdio.h>
#include <unistd.h> 
#include <stdlib.h>
bool running = true;



int main() {
    int i = 0;
    while (running == true) {
        i++;
        printf("%d\n", i);
        //system("clear");
    }
    return 0;
}