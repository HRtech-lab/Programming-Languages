#include <iostream>
#include <iomanip>
#include <algorithm>
#include <charconv>
#include <fstream>
#include <numeric>
#include <string>
#include <vector>

int main() {
    std::cout << std::setprecision(12);
    std::ifstream input("readings.csv");
    std::string line;
    if (!std::getline(input, line)) return 1;
    std::vector<int> values;
    int rejected = 0;
    while (std::getline(input, line)) {
        if (!line.empty() && line.back() == '\r') line.pop_back();
        int value;
        const auto last = line.data() + line.size();
        auto [end, error] = std::from_chars(line.data(), last, value);
        if (error == std::errc{} && end == last) values.push_back(value);
        else ++rejected;
    }
    if (input.bad() || values.empty()) return 1;
    auto [lo, hi] = std::minmax_element(values.begin(), values.end());
    std::cout << values.size() << ' ' << std::accumulate(values.begin(), values.end(), 0)
              << ' ' << *lo << ' ' << *hi << ' ' << rejected;
}
