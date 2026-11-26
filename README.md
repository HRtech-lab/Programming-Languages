# Programming Languages

Study the same small problems in nine languages, with eight lessons per language. Compare how each language handles types, control flow, collections, files and numerical error. Each language also has a workshop on a distinctive feature, such as borrowing in Rust or goroutines in Go.

## Try a short example

The [short examples](examples/README.md) cover sliding-window means in Python and run-length encoding in C++17. From the repository root, run

```sh
python examples/rolling_mean.py
```

| Course | Native runtime | Language workshop |
|---|---|---|
| [Python](Python/README.md) | Python 3.12 | Generators and sliding windows |
| [Rust](Rust/README.md) | Rust, edition 2021 | Borrowed windows and iterator lifetimes |
| [R](R/README.md) | R 4.5 | Formula models and prediction |
| [C](C/README.md) | C17 compiler | Dynamic allocation and ownership |
| [C++](C%2B%2B/README.md) | C++17 compiler | RAII and class invariants |
| [MATLAB](MATLAB/README.md) | MATLAB or GNU Octave | Matrix division and least squares |
| [JavaScript](JavaScript/README.md) | Node.js | Promises and result ordering |
| [Go](Go/README.md) | Go toolchain | Goroutines and ordered collection |
| [SQL](SQL/README.md) | SQLite 3 with window functions | Window frames and rolling averages |

## How the checks work

Every numbered folder contains the native source, a Python companion and an executed Jupyter notebook. The Python companion runs the native programme in a temporary directory, reads its actual output, checks its length and compares each value against an independent calculation. The plotted bars show the native result. Reference marks record the second calculation. In SQL, the runner executes the checked-in query through the SQLite engine included with Python.

Install Python 3, NumPy, Matplotlib and Jupyter, then install the runtime for the language you want to use. Native scripts can also be run directly from each chapter using the command in the course index. The MATLAB course includes native .m files. Its notebook outputs were recorded in GNU Octave 10.3, and all eight scripts passed a separate numerical check in [MATLAB R2025b](https://github.com/HRtech-lab/HRtech-lab/actions/runs/45731606690).

[Python dependencies](requirements.txt) · [Native runtime driver](course_runner.py) · [MIT licence](LICENSE)
