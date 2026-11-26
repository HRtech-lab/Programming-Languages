#include <stdio.h>
#include <stdlib.h>

int main(void) {
    const int input[] = {2, 4, 8, 1, 3, 7};
    const size_t n = sizeof input / sizeof *input, width = 3;
    double *means = malloc((n - width + 1) * sizeof *means);
    if (!means) return 1;
    int sum = 0;
    for (size_t i = 0; i < n; ++i) {
        sum += input[i];
        if (i >= width) sum -= input[i-width];
        if (i+1 >= width) means[i+1-width] = (double)sum / width;
    }
    for (size_t i = 0; i <= n-width; ++i) printf("%.12g ", means[i]);
    free(means);
    return 0;
}
