# Packaging

- [Packaging](#packaging)
  - [Restructure the package](#restructure-the-package)
  - [Build the package](#build-the-package)
  - [Publish the package](#publish-the-package)
    - [IMPORTANT NOTE](#important-note)
  - [Check your package install with pip](#check-your-package-install-with-pip)

As mentioned on the [official documentation of `setuptools`](https://setuptools.pypa.io/en/latest/userguide/quickstart.html#resources-on-python-packaging)
> Packaging in Python is hard. Here we provide a list of links for those that want to learn more.

Nevertheless, the way was already paved for you

- [`src/`](../src/) structure
- [`setup.cfg`](../setup.cfg), [`pyproject.toml`](../pyproject.toml), [`setup.py`](../setup.py) files
- [`README.md`](../README.md) and [`LICENCE`](../LICENSE) files

However, the project is currently made of the packages `lab1`, `lab2`, ... which can be imported  using `from/import labX ...` (when the sdia-python virtual environment is activated).
This may conflict with another course where you may also want to import the corresponding `lab*` files.

- Wouldn't it be clearer to import them using `from/import sdia_python.labX ...` instead?
- How about we turn the project into a real Python package, so that you can share your project using  a command like `pip install your-package-name`?

See also

- <https://packaging.python.org/tutorials/packaging-projects/>
- <https://github.com/pypa/sampleproject>

## Restructure the package

**Your instructor could have done it for you from the beginning, but instead left it as a Python+git+VSCode exercise!**

1. **FIRST COMMIT YOUR LAST CHANGES**

    ```bash
    git status
    git add file1 file2 ...
    git commit -m "Write an explicit message"
    ```

2. Create a new branch `packaging`

    ```bash
    git branch --list
    # "*" symbol indicates current working branch
    git branch packaging
    git switch packaging
    # git switch --create packaging
    git branch
    # same as git branch --list
    git log --oneline
    ```

3. Move `lab*` folders to a new folder `src/sdia_python` which only contains a blank `__init__.py` file. To do this,

   - use the command line and let `git` follow what you're doing

      ```bash
      # cd path-to-your-project
      # conda activate sdia-python
      #################################
      # MacOS
      mkdir src/sdia_python
      touch src/sdia_python/__init__.py
      git mv src/sdia_python/lab* src/sdia_python
      git status
      git add src/sdia_python
      git status
      # Windows
      mkdir src\sdia_python
      type NUL > src\sdia_python\__init__.py
      # create an empty file src\sdia_python\__init__.py
      git mv src\lab1 src\sdia_python
      git mv src\lab2 src\sdia_python
      git mv src\lab3 src\sdia_python
      git mv src\lab4 src\sdia_python
      git mv src\lab5 src\sdia_python
      git mv src\lab6 src\sdia_python
      git status
      git add src\sdia_python
      git status
      #################################
      ```

4. Update the package imports: the source files have been moved, so that imports must be updated accordingly (`from/import  lab...` -> `from sdia_python.lab...`). From VSCode, you can use `CMD/CTRL + Maj + H` or `CMD/CTRL + Maj + P + Search: Replace in files`, enter the successive "search - replace" pairs in the corresponding cells, remove the current `packaging.md` file from the list and click the "Replace All" button (you might need save the files just modified)

   - from lab - from sdia_python.lab
   - import lab - import sdia_python.lab
   - .. automodule:: lab - .. automodule:: sdia_python.lab
   - src/lab - src/sdia_python/lab

   - Finally, run

        ```bash
        git status
        git add --update
        git status
        ```

5. Reinstall the package in **EDITABLE** mode, to update the new paths to the package

    ```bash
    # cd path-to-your-project
    # conda activate sdia-python
    # safer but not mandatory a priori
    pip uninstall sdia-python
    pip install -e .
    ```

6. Check your tests still run and pass against the restructured package

    ```bash
    # cd path-to-your-project
    # conda activate sdia-python
    pytest
    ```

7. Check your documentation builds correctly against the restructured package

    ```bash
    # cd path-to-your-project
    # conda activate sdia-python
    sphinx-build -b html docs docs/_build/html
    ```

8. Commit your changes, once tests pass and documentation builds

    ```bash
    # cd path-to-your-project
    # conda activate sdia-python
    git status
    git add -u
    # Moved files should appear in green in the staging area "Changes to be committed:"
    # Modified files should appear in red in the "Changes not staged for commit:"
    git commit -m "Restructure the package into src/sdia_python, update imports accordingly"
    ```

9. If everything works and you're satisfied with this new structure, you can merge your `packaging` branch into your `main` branch

    ```bash
    git log --oneline
    git switch main
    git log --oneline
    git merge packaging
    git log --oneline
    ```

## Build the package

0. Install the [PyPA `build` tool](https://pypa-build.readthedocs.io/en/latest/index.html)

    ```bash
    # cd path-to-your-project
    # conda activate sdia-python
    pip install build
    ```

1. Build the package

    ```bash
    # cd path-to-your-project
    # conda activate sdia-python
    # MacOS
    rm dist/*
    python -m build
    # Windows
    rmdir dist
    python -m build
    ```

## Publish the package

0. `conda install twine`
1. Create a [TestPyPI account](https://test.pypi.org/account/register/) (consider using the same username as your GitHub username)
2. Before uploading/publishing your package, make sure that
    - the [`your-package-name` isn't already used on TestPyPI](https://test.pypi.org/search/?q=package-name), otherwise you need to consider changing `[metedata] name = sdia-python` in [`setup.cfg`](../setup.cfg), like `sdia-python-username`.
    - your `[metedata] version =` in [`setup.cfg`](../setup.cfg) differs from what is already present on TestPyPI
      - you may consider setting `version = 0.1.0-alpha.1`
      - see also [semantic versioning](https://semver.org/)!
    - otherwise
      - apply the necessary modifications
      - **SAVE YOUR FILE**
      - re-[build the package](#build-the-package)
3. [Upload/publish your package to TestPI](https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives)

    ```bash
    twine check dist/*
    twine upload --repository testpypi dist/*
    ```

4. Check the result on <https://test.pypi.org/project/sdia-python-username>

### IMPORTANT NOTE

Recall that your package was previously installed in editable mode (see 4. in [Restructure the package](#restructure-the-package)) under the name `sdia-python` with version `0.1.0` (check the info using `conda list`).

Hence, the modifications made in [`setup.cfg`](../setup.cfg), namely `name = sdia-python-username` and `version = your-version` introduce semantic conflicts with the current installation.

Besides, this may in turn lead to conflicts with your partner's version of the [`setup.cfg`](../setup.cfg) file.

You can consider restoring the file to its previous version

```bash
git status
git diff setup.cfg
git restore setup.cfg
```

## Check your package install with pip

0. Create a new environment.

   ```bash
   conda deactivate
   conda create -n sdia-python-testpypi python=3.8 pip
   ```

1. Activate your new environment
   - `conda activate sdia-python-testpypi`

2. [Install your package from TestPyPI](https://packaging.python.org/guides/using-testpypi/#using-testpypi-with-pip)
   - `pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ sdia-python-username`

3. `conda list` find the line corresponding to `sdia-python-username`
