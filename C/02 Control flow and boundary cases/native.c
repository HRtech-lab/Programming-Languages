#include <stdio.h>

int main(void) {
    const int values[] = {-4, 0, 5, 12, 18, 25, 31};
    size_t counts[3] = {0};
    for (size_t i = 0; i < sizeof values / sizeof *values; ++i) {
        int value = values[i];
        size_t bucket = value <= 0 ? 0u : (value < 20 ? 1u : 2u);
        ++counts[bucket];
    }
    printf("%zu %zu %zu", counts[0], counts[1], counts[2]);
    return 0;
}
