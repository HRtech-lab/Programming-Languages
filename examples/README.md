# Runnable examples

Run these commands from the repository root.

## Rolling mean

Use a Python generator to compute complete sliding-window means in one pass.

```sh
python examples/rolling_mean.py
```

## Run lengths

Group consecutive equal values using C++17 structured bindings.

```sh
c++ -std=c++17 examples/run_lengths.cpp -o /tmp/run_lengths
/tmp/run_lengths
```
