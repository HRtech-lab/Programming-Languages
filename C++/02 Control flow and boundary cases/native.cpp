#include <iostream>
#include <iomanip>
#include <array>

int main() {
    std::cout << std::setprecision(12);
    std::array<int, 3> counts{};
    const auto classify = [](int value) {
        if (value <= 0) return 0;
        if (value < 20) return 1;
        return 2;
    };
    for (int value : {-4, 0, 5, 12, 18, 25, 31}) ++counts.at(classify(value));
    for (auto count : counts) std::cout << count << ' ';
}
