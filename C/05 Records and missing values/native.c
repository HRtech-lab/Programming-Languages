#include <stdio.h>
#include <stdbool.h>

struct reading { char name; int value; bool present; };

int main(void) {
    const struct reading rows[] = {{'A',3,true},{'B',8,true},{'A',5,true},{'C',2,true},{'B',0,false}};
    int sums[3] = {0}, counts[3] = {0};
    for (size_t i = 0; i < sizeof rows / sizeof *rows; ++i) {
        if (!rows[i].present) continue;
        size_t k = rows[i].name == 'A' ? 0u : (rows[i].name == 'B' ? 1u : 2u);
        sums[k] += rows[i].value;
        ++counts[k];
    }
    for (size_t k = 0; k < 3; ++k) {
        if (!counts[k]) return 1;
        printf("%.8g ", (double)sums[k] / counts[k]);
    }
    return 0;
}
