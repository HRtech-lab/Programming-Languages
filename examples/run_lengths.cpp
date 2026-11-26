// Group consecutive equal values in a single traversal of a vector.
#include <cassert>
#include <cstddef>
#include <iostream>
#include <utility>
#include <vector>

using Run = std::pair<int, std::size_t>;

std::vector<Run> run_lengths(const std::vector<int>& values) {
    std::vector<Run> runs;
    for (int value : values) {
        if (runs.empty() || runs.back().first != value) {
            runs.emplace_back(value, 1);
        } else {
            ++runs.back().second;
        }
    }
    return runs;
}

int main() {
    const auto runs = run_lengths({4, 4, 2, 4, 4, 4});
    const std::vector<Run> expected{{4, 2}, {2, 1}, {4, 3}};
    assert(runs == expected);
    assert(run_lengths({}).empty());
    for (const auto& [value, count] : runs) {
        std::cout << value << " occurs " << count << " time(s) in this run\n";
    }
}
