#include <stdio.h>

void thing() {
  for (double i = 0; i < 100; i++) {
    printf("hello\n", i);
  }
}

int main() {
  printf("hello\n");
  thing();
}