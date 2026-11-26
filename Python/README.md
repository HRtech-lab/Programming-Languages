# Python

Eight lectures use small programmes whose outputs can be checked independently. Read the [complete lecture notes](LECTURES.md) from start to finish or follow individual worked notebooks below. Each chapter includes its native source, a Python companion, numerical output, a figure and an exercise.

## Run the native source

Use Python 3.12. In the directory containing the listing:

```sh
python native.py
```

The file-input lecture expects readings.csv in the working directory. The Python companion handles the working directory for you.

## Worked lectures

| Lecture | Question or experiment |
|---|---|
| [01. Values and numeric types](01%20Values%20and%20numeric%20types/README.md) | Convert five readings from Celsius to Fahrenheit and examine where arithmetic changes type. |
| [02. Control flow and boundary cases](02%20Control%20flow%20and%20boundary%20cases/README.md) | Assign each observation to a band, including the observations exactly on a boundary. |
| [03. Collections and prefix sums](03%20Collections%20and%20prefix%20sums/README.md) | Keep the balance after every signed change, including a negative change and a zero. |
| [04. Bisection and numerical functions](04%20Bisection%20and%20numerical%20functions/README.md) | Approximate square roots by repeatedly halving a bracket. |
| [05. Records and missing values](05%20Records%20and%20missing%20values/README.md) | Compute mean readings by instrument while retaining the difference between zero and an absent reading. |
| [06. File input and validation](06%20File%20input%20and%20validation/README.md) | Read a one-column file and report the valid count, sum, range and number of rejected records. |
| [07. Generators and sliding windows](07%20Generators%20and%20sliding%20windows/README.md) | Follow a feature that shapes how this language is used in practice. |
| [08. Online variance and testing](08%20Online%20variance%20and%20testing/README.md) | Compute the population variance after each reading without losing its small variation around a large baseline. |

[Complete lecture notes](LECTURES.md) · [Language reference](https://docs.python.org/3/tutorial/) · [Shared environment](../README.md)
