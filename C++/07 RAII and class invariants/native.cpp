#include <iostream>
#include <iomanip>
#include <deque>
#include <stdexcept>
#include <vector>

class RollingMean {
    std::deque<double> data;
    std::size_t width;
    double total = 0;
public:
    explicit RollingMean(std::size_t n) : width(n) {
        if (!n) throw std::invalid_argument("zero width");
    }
    void push(double value) {
        data.push_back(value);
        total += value;
        if (data.size() > width) { total -= data.front(); data.pop_front(); }
    }
    bool full() const { return data.size() == width; }
    double value() const {
        if (!full()) throw std::logic_error("incomplete window");
        return total / width;
    }
};

int main() {
    std::cout << std::setprecision(12);
    RollingMean mean(3);
    for (int value : {2, 4, 8, 1, 3, 7}) {
        mean.push(value);
        if (mean.full()) std::cout << mean.value() << ' ';
    }
}
