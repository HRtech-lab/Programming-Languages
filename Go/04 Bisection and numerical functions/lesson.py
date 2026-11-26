"""Bisection and numerical functions

Approximate square roots by repeatedly halving a bracket.

The Go Programming Language Specification
https://go.dev/ref/spec"""

from pathlib import Path
import sys, math, statistics
import numpy as np
import matplotlib.pyplot as plt

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent.parent))
from course_runner import run_native


def main():
    x = [0, 0.5, 2, 10, 25]
    expected = np.asarray([math.sqrt(v) for v in x], dtype=float)
    engine, stdout = run_native(here / "native.go")
    observed = np.asarray([float(v) for v in stdout.split()])
    assert observed.shape == expected.shape
    np.testing.assert_allclose(observed, expected, rtol=2e-7, atol=2e-7)
    print("Runtime:", engine)
    print("Native stdout:", stdout.strip())
    print("Largest absolute difference:", f"{np.max(np.abs(observed-expected)):.3g}")

    labels = [str(v) for v in x]
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
    ax.set(xticks=positions, xticklabels=labels, xlabel="Radicand", ylabel="Square root")
    ax.legend(fontsize=8)
    plt.show()


if __name__ == "__main__":
    main()
