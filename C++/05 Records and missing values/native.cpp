#include <iostream>
#include <iomanip>
#include <map>
#include <optional>
#include <utility>
#include <vector>

int main() {
    std::cout << std::setprecision(12);
    const std::vector<std::pair<char, std::optional<int>>> rows{
        {'A', 3}, {'B', 8}, {'A', 5}, {'C', 2}, {'B', std::nullopt}};
    std::map<char, std::pair<int, int>> groups;
    for (const auto& [name, x] : rows) {
        if (!x) continue;
        auto& [sum, count] = groups[name];
        sum += *x;
        ++count;
    }
    for (const auto& entry : groups) {
        const auto& [sum, count] = entry.second;
        std::cout << static_cast<double>(sum) / count << ' ';
    }
}
