#include <stdio.h>
#include <math.h>
#include <stdbool.h>

static bool root(double n, double *result) {
    if (!isfinite(n) || n < 0 || !result) return false;
    double lo = 0, hi = fmax(1, n);
    if (n == 0) { *result = 0; return true; }
    for (unsigned i = 0; i < 55; ++i) {
        double mid = (lo + hi) / 2;
        if (mid * mid < n) lo = mid; else hi = mid;
    }
    *result = (lo + hi) / 2;
    return true;
}

int main(void) {
    const double values[] = {0, 0.5, 2, 10, 25};
    for (size_t i = 0; i < 5; ++i) {
        double answer;
        if (!root(values[i], &answer)) return 1;
        printf("%.12g ", answer);
    }
    return 0;
}
