#include <iostream>
#include <iomanip>
#include <algorithm>
#include <stdexcept>

double root(double n) {
    if (n < 0) throw std::domain_error("negative radicand");
    if (n == 0) return 0;
    double lo = 0, hi = std::max(n, 1.0);
    for (int i = 0; i < 55; ++i) {
        const double mid = (lo + hi) / 2;
        if (mid * mid < n) lo = mid; else hi = mid;
    }
    return (lo + hi) / 2;
}

int main() {
    std::cout << std::setprecision(12);
    for (double x : {0., 0.5, 2., 10., 25.}) std::cout << root(x) << ' ';
}
