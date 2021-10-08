# To go further

A list of topics and links to resources that may help you learn and improve.

In particular, I find [Real Python](https://realpython.com/) a great (mostly free) and high quality place to learn new Python stuff.

## Run Python scripts

- [Real Python tutorial](https://realpython.com/run-python-scripts/)

Simply run `python file.py`

```python
# file.py


def addition(x, y):
    return x


def main():
    x, y = 1, 2
    result = addition(x, y)
    print(result)


if __name__ == "__main__":
    main()
```

## Run tests using VSCode

See the [Testing](https://code.visualstudio.com/docs/python/testing) section of the VSCode documentation.

## Debug Python code using VSCode

The configuration file [.vscode/launch.json](.vscode/launch.json) contains two configurations for debugging

1. Python generic
2. Python test files

For more details, check out the documentation

- [Debugging](https://code.visualstudio.com/docs/python/debugging),
- [Debug Tests](https://code.visualstudio.com/docs/python/testing#_debug-tests).

## Play with paths

Use [`pathlib`](https://docs.python.org/3/library/pathlib.html)

- [Real Python tutorial](https://realpython.com/python-pathlib/)

## Data structures

- [Real Python tutorial](https://realpython.com/python-data-structures/)

### Numpy arrays

- [`numpy` official documentation](https://numpy.org/learn/)
- [Real Python tutorial](https://realpython.com/numpy-array-programming/)

### Pandas DataFrames

- [`pandas` official documentation](https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html#)
- [Real Python tutorial](https://realpython.com/pandas-dataframe/)

## Plotting

[`matplotlib`](https://matplotlib.org/stable/tutorials/index.html) is the main tool on which many other tools are built on, like

- [`pandas` visualization](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html)
- [`seaborn`](https://seaborn.pydata.org/)

### Tip for matplotlib users

To make consistent plots (size/font of labels/ticks, width of lines/points) consider using a [`my_style.mplstyle`](https://matplotlib.org/stable/tutorials/introductory/customizing.html) file and import it in your `.py` file or your notebook ; see also [this concise tutorial](https://towardsdatascience.com/how-to-create-and-use-custom-matplotlib-style-sheet-9393f498063).

### See also

- [`plotnine`](https://plotnine.readthedocs.io/en/stable/)
- [`plotly`](https://plotly.com/python/)
- [`bokeh`](https://bokeh.org/)

## Performance

### Timing

- [`timeit`](https://docs.python.org/3/library/timeit.html)
- [Real Python tutorial](https://realpython.com/python-timer/#python-timers)

#### Anywhere

[`timeit`](https://docs.python.org/3/library/timeit.html)

```python
import timeit

setup_code = """
from sdia_python.lab1.functions import is_unique
x = [1, 2, 3]
"""

main_code = """
is_unique(x)
"""

print(timeit.timeit(stmt=main_code, setup=setup_code, number=10))
print(timeit.repeat(stmt=main_code, setup=setup_code, number=10, repeat=5))
```

#### In your notebook

See the [IPython documentation](https://ipython.readthedocs.io/en/stable/interactive/magics.html?highlight=timeit#cell-magics)

- inline `%timeit code-to-time`
- in cell

  ```bash
  %%timeit
  code-to-time
  ```

### Profiling

> A [profile](https://docs.python.org/3/library/profile.html#module-cProfile) is a set of statistics that describes how often and for how long various parts of the program executed

It will help you identify the bottlenecks in your code, so that you can focus on them to improve the performance of your code.

### Multiprocessing

- [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html)
- [Machine Learning Plus tutorial](tps://www.machinelearningplus.com/python/parallel-processing-python/)
