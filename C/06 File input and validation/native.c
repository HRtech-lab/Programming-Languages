#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <limits.h>
#include <ctype.h>

int main(void) {
    FILE *input = fopen("readings.csv", "r");
    if (!input) return 1;
    char line[128];
    if (!fgets(line, sizeof line, input)) { fclose(input); return 1; }
    long lo = LONG_MAX, hi = LONG_MIN, sum = 0;
    size_t count = 0, rejected = 0;
    while (fgets(line, sizeof line, input)) {
        char *end;
        errno = 0;
        long value = strtol(line, &end, 10);
        if (end == line || errno == ERANGE) { ++rejected; continue; }
        while (isspace((unsigned char)*end)) ++end;
        if (*end) { ++rejected; continue; }
        if (value < lo) lo = value;
        if (value > hi) hi = value;
        sum += value;
        ++count;
    }
    int failed = ferror(input);
    fclose(input);
    if (failed || !count) return 1;
    printf("%zu %ld %ld %ld %zu", count, sum, lo, hi, rejected);
    return 0;
}
