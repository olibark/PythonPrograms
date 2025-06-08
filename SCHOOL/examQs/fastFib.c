#include <stdio.h>

typedef unsigned long long unsignedLL;

void multiply(unsignedLL F[2][2], unsignedLL M[2][2]) {
    unsignedLL x = F[0][0]*M[0][0] + F[0][1]*M[1][0];
    unsignedLL y = F[0][0]*M[0][1] + F[0][1]*M[1][1];
    unsignedLL z = F[1][0]*M[0][0] + F[1][1]*M[1][0];
    unsignedLL w = F[1][0]*M[0][1] + F[1][1]*M[1][1];

    F[0][0] = x;
    F[0][1] = y;
    F[1][0] = z;
    F[1][1] = w;
}

void power(unsignedLL F[2][2], unsignedLL n) {
    unsignedLL result[2][2] = {{1, 0}, {0, 1}}; // Identity matrix

    while (n > 0) {
        if (n % 2 == 1)
            multiply(result, F);
        multiply(F, F);
        n /= 2;
    }

    // Copy result back into F
    F[0][0] = result[0][0];
    F[0][1] = result[0][1];
    F[1][0] = result[1][0];
    F[1][1] = result[1][1];
}

unsignedLL fast_fibonacci(unsignedLL n) {
    if (n == 0) return 0;
    unsignedLL F[2][2] = {{1, 1}, {1, 0}};
    power(F, n - 1);
    return F[0][0];
}

int main() {
    unsignedLL n;
    printf("Enter n: ");
    scanf("%llu", &n);
    printf("Fibonacci(%llu) = %llu\n", n, fast_fibonacci(n));
    return 0;
}
