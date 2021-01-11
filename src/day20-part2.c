#include <stdio.h>
#include <stdlib.h>

long house(long n) {
    long total = n;
    for (long i = 1; i <= (n / 2); i++) {
        if (n / i <= 50 && n % i == 0) {
            total += i;
        }
    }
    return 11 * total;
}

int main(void) {
    FILE *f = fopen("resources/day20.txt", "r");
    long n;
    fscanf(f, "%ld", &n);
    fclose(f);
    long part2 = 0;
    printf("Looking for %ld...\n", n);
    while (house(part2) < n) {
        part2 += 1; if (part2 % 10000 == 0) {
            printf("%ld: %ld\n", part2, house(part2));
        }
    }
    printf("\nPart 2: %ld\n", part2);
    return 0;
}
