#include <iostream>
#include <iomanip>
#include <array>

int main() {
    std::cout << std::setprecision(12);
    constexpr std::array celsius{-10, 0, 10, 20, 30};
    for (auto c : celsius) std::cout << c * 9.0 / 5.0 + 32.0 << ' ';
}
