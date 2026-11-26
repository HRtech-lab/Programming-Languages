#include <iostream>
#include <iomanip>

struct Moments {
    unsigned count{};
    double mean{}, m2{};
    double update(double x) {
        double delta = x - mean;
        mean += delta / ++count;
        m2 += delta * (x - mean);
        return m2 / count;
    }
};

int main() {
    std::cout << std::setprecision(12);
    Moments state;
    for (double x : {1., 2., 4., 5.}) std::cout << state.update(1e9 + x) << ' ';
}
