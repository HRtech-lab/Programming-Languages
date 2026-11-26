"""Collections and prefix sums

Keep the balance after every signed change, including a negative change and a zero.

MDN, JavaScript Guide
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide"""

from pathlib import Path
import sys, math, statistics
import numpy as np
import matplotlib.pyplot as plt

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent.parent))
from course_runner import run_native


def main():
    x = [3, -1, 4, -2, 0, 2]
    expected = np.asarray([sum(x[:i]) for i in range(1, len(x) + 1)], dtype=float)
    engine, stdout = run_native(here / "native.js")
    observed = np.asarray([float(v) for v in stdout.split()])
    assert observed.shape == expected.shape
    np.testing.assert_allclose(observed, expected, rtol=2e-7, atol=2e-7)
    print("Runtime:", engine)
    print("Native stdout:", stdout.strip())
    print("Largest absolute difference:", f"{np.max(np.abs(observed-expected)):.3g}")

    labels = [str(v) for v in range(1, 7)]
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
        xticks=positions, xticklabels=labels, xlabel="Observation", ylabel="Cumulative balance"
    )
    ax.legend(fontsize=8)
    plt.show()


if __name__ == "__main__":
    main()
