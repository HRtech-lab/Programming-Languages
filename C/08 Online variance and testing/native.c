#include <stdio.h>

struct moments { unsigned count; double mean; double m2; };

int main(void) {
    struct moments s = {0};
    const double offsets[] = {1, 2, 4, 5};
    for (size_t i = 0; i < 4; ++i) {
        double x = 1e9 + offsets[i];
        double delta = x - s.mean;
        s.mean += delta / ++s.count;
        s.m2 += delta * (x - s.mean);
        printf("%.12g ", s.m2 / s.count);
    }
    return 0;
}
