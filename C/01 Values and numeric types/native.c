#include <stdio.h>

int main(void) {
    const int celsius[] = {-10, 0, 10, 20, 30};
    for (size_t i = 0; i < sizeof celsius / sizeof *celsius; ++i) {
        printf("%.8g ", celsius[i] * 9.0 / 5.0 + 32.0);
    }
    return 0;
}
