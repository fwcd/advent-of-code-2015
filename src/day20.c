#include <stdio.h>
#include <stdlib.h>

long house(long n) {
    long total = n;
    for (long i = 1; i <= (n / 2); i++) {
        if (n % i == 0) {
            total += i;
        }
    }
    return 10 * total;
}

int main(void) {
    FILE *f = fopen("resources/day20.txt", "r");
    long n;
    fscanf(f, "%ld", &n);
    fclose(f);
    long part1 = 0;
    printf("Looking for %ld...\n", n);
    while (house(part1) < n) {
        part1 += 1;
        if (part1 % 10000 == 0) {
            printf("%ld: %ld\n", part1, house(part1));
        }
    }
    printf("\nPart 1: %ld\n", part1);
    return 0;
}
