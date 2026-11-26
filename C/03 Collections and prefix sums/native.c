#include <stdio.h>

static void prefix_sum(const int *input, int *output, size_t length) {
    int total = 0;
    for (size_t i = 0; i < length; ++i) {
        total += input[i];
        output[i] = total;
    }
}

int main(void) {
    const int changes[] = {3, -1, 4, -2, 0, 2};
    int balances[6];
    prefix_sum(changes, balances, 6);
    for (size_t i = 0; i < 6; ++i) printf("%d ", balances[i]);
    return 0;
}
