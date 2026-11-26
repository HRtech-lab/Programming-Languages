"""Online variance and testing

Compute the population variance after each reading without losing its small variation around a large baseline.

MDN, JavaScript Guide
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide
Welford, corrected sums of squares (1962)
https://doi.org/10.1080/00401706.1962.10490022"""

from pathlib import Path
import sys, math, statistics
import numpy as np
import matplotlib.pyplot as plt

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent.parent))
from course_runner import run_native


def main():
    x = [1_000_000_000 + i for i in (1, 2, 4, 5)]
    expected = np.asarray(
        [statistics.pvariance(x[:i]) for i in range(1, len(x) + 1)], dtype=float
    )
    engine, stdout = run_native(here / "native.js")
    observed = np.asarray([float(v) for v in stdout.split()])
    assert observed.shape == expected.shape
    np.testing.assert_allclose(observed, expected, rtol=2e-7, atol=2e-7)
    print("Runtime:", engine)
    print("Native stdout:", stdout.strip())
    print("Largest absolute difference:", f"{np.max(np.abs(observed-expected)):.3g}")

    labels = ["1", "2", "3", "4"]
    positions = np.arange(len(labels))
    fig, ax = plt.subplots(figsize=(6.1, 3), constrained_layout=True)
    ax.bar(positions, observed, color="#367b80", alpha=0.82, label="Native output")
    ax.plot(
        positions,
        expected,
        linestyle="none",
        marker="_",
        markersize=13,
        color="#713925",
        label="Reference",
    )
    ax.set(
        xticks=positions, xticklabels=labels, xlabel="Prefix length", ylabel="Population variance"
    )
    ax.legend(fontsize=8)
    plt.show()


if __name__ == "__main__":
    main()
