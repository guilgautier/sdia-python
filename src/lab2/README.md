# Tests, docstrings and BoxWindow class

## Tests

> The [`pytest`](https://docs.pytest.org/en/6.2.x/) framework makes it easy to write small tests, yet scales to support complex functional testing.

It is **very important** to write and run unit tests, to make sure your code works (at least) as expected both for you as you develop but also for other users.

### Install testing dependencies

In this project,

- `pytest` is listed as a development dependency, see [`[options.extras_require]` section of the `setup.cfg`](../../setup.cfg) file,

    ```bash
    # cd path-to-your-project
    # conda activate sdia-python
    pip install -e ".[dev]"
    ```

The configuration of `pytest` is defined in the [`[tool.pytest.ini_options]` section of the `pyproject.toml` file](https://docs.pytest.org/en/latest/reference/customize.html#pyproject-toml).

### Run tests

Unit tests of the package are declared in [`tests/labX/test_*.py`](../../tests/) files as `test_*` functions with a simple `assert` statement,

Run the package test suite with

```bash
# cd path-to-your-project
# conda activate sdia-python
pytest  # tests/ tests/lab1/ tests/lab1/test_is_unique.py
```

### Exercise 1

Test your code from `lab1` and make sure they all pass.

## Documentation

> [Sphinx](https://www.sphinx-doc.org/en/master/index.html)  is a tool that makes it easy to create intelligent and beautiful documentation.

Sphinx is in charge of building the documentation and generating HTML output, but also PDF, epub, ...

Documentaion is an **essential** part of your project; you must take some time to document you project properly.

See also:

- [sphinx documentation](https://www.sphinx-doc.org/en/master/usage/configuration.html)

### Docstrings

[Documenting Python code](https://realpython.com/documenting-python-code/) is **key** to your project.

**You must take some time to document your functions, classes, etc.**

In this project, we suggest to use

- the ["Python Docstring Generator" extension](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring) may be of great help, [`.vscode/extensions.json`](../../.vscode/extensions.json) file
- the Google docstring format as defined at  `"autoDocstring.docstringFormat": "google"` in the [`.vscode/settings.json`](../../.vscode/settings.json) file
  - note that the `"sphinx.ext.napoleon"` is required to support google and numpy docstring style as defined in in the [`docs/conf.py`](../../docs/conf.py) file

See also:

- [docstrings conventions](https://www.python.org/dev/peps/pep-0257/)

### Install documentation dependencies

Documentation dependencies are listed as in [`[options.extras_require]` section of the `setup.cfg`](../../setup.cfg) file,

  ```bash
  # cd path-to-your-project
  # conda activate sdia-python
  pip install ".[docs]"
  ```

### Generate the documentation

The source files of the documentation are simply `.rst` ([reStructuredText](https://docutils.sourceforge.io/rst.html)) or `.md` (Markdown) files.
However we suggest using reST markup to keep the same syntax and format as used for writing [Python docstings](https://devguide.python.org/documenting/).

The documentation is configured in the [`docs/conf.py`](../../docs/conf.py) file.

To generate the documentation locally, i.e., on your machine, you can either use

  ```bash
  # cd path-to-your-project
  # conda activate sdia-python
  sphinx-build -b html docs docs/_build/html
  ```

  and navigate the documentation

  ```bash
  open docs/_build/html/index.html
  ```

**Note:** Any change made in the source `.py` files or the `docs/conf.py` file require rebuilding the documentation.

### Exercise 2

- Edit the metadata of the package defined in [`docs/conf.py`](../../docs/conf.py)
- Write good docstrings your code from `lab1`,
- Generate the corresponding documentation
- [BONUS] customize the documentation with some new sections, LaTeX, etc.

## BoxWindow class

- Edit the class `BoxWindow` in [src/lab2/box_window.py](./box_window.py)
- Run the tests from [`tests/lab2/`](../../tests/lab2)
- Complete the class body
  - write the docstrings
  - make sure the current tests pass
- Write new tests that test various use cases of the different methods
- [Bonuses]
  - create the counterpart `BallWindow` class that works at least in 1D and 2D
  - estimate the value of `pi` using rejection sampling
