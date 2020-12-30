#include <stdio.h>
#include <stdlib.h>

long house(long n) {
    long total = n
    for (long i = 0; i <= (total / 2); i++) {
        if (n % i == 0) {
            total += i;
        }
    }
    return 10 * total;
}

int main(void) {
    FILE *f = fopen("resources/day20.txt");
    long n;
    fscanf(f, "%d", &n);
    fclose(f);
    long part1 = 0;
    while (house(part1) < n) {
        part1 += 1;
        if (part1 % 1000 == 0) {
            printf("\r%ld", part1);
        }
    }
    printf("\nPart 1: %ld\n", part1);
    return 0;
}
