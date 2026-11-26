"""Control flow and boundary cases

Assign each observation to a band, including the observations exactly on a boundary.

C language reference and standard revisions
https://en.cppreference.com/w/c/language"""

from pathlib import Path
import sys, math, statistics
import numpy as np
import matplotlib.pyplot as plt

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent.parent))
from course_runner import run_native


def main():
    x = [-4, 0, 5, 12, 18, 25, 31]
    expected = np.asarray(
        [sum(v <= 0 for v in x), sum(0 < v < 20 for v in x), sum(v >= 20 for v in x)], dtype=float
    )
    engine, stdout = run_native(here / "native.c")
    observed = np.asarray([float(v) for v in stdout.split()])
    assert observed.shape == expected.shape
    np.testing.assert_allclose(observed, expected, rtol=2e-7, atol=2e-7)
    print("Runtime:", engine)
    print("Native stdout:", stdout.strip())
    print("Largest absolute difference:", f"{np.max(np.abs(observed-expected)):.3g}")

    labels = ["≤0", "(0,20)", "≥20"]
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
    ax.set(xticks=positions, xticklabels=labels, xlabel="Band", ylabel="Count")
    ax.legend(fontsize=8)
    plt.show()


if __name__ == "__main__":
    main()
