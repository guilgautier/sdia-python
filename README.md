# SDIA - Python

- [SDIA - Python](#sdia---python)
  - [Get the project](#get-the-project)
  - [Set up your working environment](#set-up-your-working-environment)
    - [Virtual environment](#virtual-environment)
      - [Create a virtual environment](#create-a-virtual-environment)
      - [Activate a virtual environment](#activate-a-virtual-environment)
      - [Deactivate a virtual environment](#deactivate-a-virtual-environment)
    - [Install the project in editable mode](#install-the-project-in-editable-mode)
  - [Integrated Development Environment - Visual Studio Code](#integrated-development-environment---visual-studio-code)
  - [Notebooks](#notebooks)

Python course given to students enrolled in [Parcours DATA - Science des Données et Intelligence Artificielle (SDIA)](http://pierrechainais.ec-lille.fr/Centrale/Option_DAD/Accueil.html) managed by [Pierre Chainais](http://pierrechainais.ec-lille.fr/) at [Ecole Centrale de Lille](https://centralelille.fr/).

Some material is inspired and/or borrowed from courses previously given by:

- [Pierre-Antoine Thouvenin](https://pthouvenin.github.io/) at [Ecole Centrale de Lille - Data Science and Artificial Intelligence (SDIA)](http://pierrechainais.ec-lille.fr/Centrale/Option_DAD/Accueil.html), and
- [Guillermo Polito](https://guillep.github.io/) at [Université de Lille - M2 Data Science](https://www.univ-lille.fr/formations/fr-00020709.html).

## Get the project

From the [source page](https://github.com/guilgautier/sdia-python), you can either

- [Download](https://github.com/guilgautier/sdia-python/archive/refs/heads/master.zip) the project
  - Code (green button) -> Download zip

- Clone the repository

  ```bash
  cd <parent-directory-of-your-project>
  git clone https://github.com/guilgautier/sdia-python.git
  ```

- [Fork](https://github.com/guilgautier/sdia-python/fork) and clone your own copy of the repository
  - This will allow you to propose modifications via [Pull Requests (PRs)](https://github.com/guilgautier/sdia-python/fork)

  ```bash
  cd <parent-directory-of-your-project>
  git clone https://github.com/<your-username>/sdia-python.git
  ```

## Set up your working environment

We will use [`conda`](https://conda.io/projects/conda/en/latest/index.html) to manage Python packages and virtual environments

See also the [`conda` cheatsheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf).

### Virtual environment

#### Create a virtual environment

> A [virtual environment](https://docs.python.org/3/tutorial/venv.html) is a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages.

It is always good practice to work in a virtual environment, isolated from your other Python projects.

The [environment.yml](./environment.yml) file contains the list of the main packages that will be installed when creating the environment

```bash
cd sdia-python
# conda env list
conda env create -f environment.yml
```

See also

- [Conda as an environment manager](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
- [Conda cheatsheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)

#### Activate a virtual environment

```bash
# cd sdia-python
conda env list
conda activate sdia-python
# prefix (sdia-python) should appear
```

#### Deactivate a virtual environment

```bash
# cd sdia-python
# conda activate sdia-python
conda deactivate
# prefix (sdia-python) should disappear
```

### Install the project in editable mode

In order to be able to import your code in various places of your project (source files, test files, noteboooks), like

```python
import lab1
from lab1.xxx import yyy
```

> You can install a project in "editable" or "develop" mode while you’re working on it.
> When installed as editable, a project can be edited in-place without reinstallation:
> changes to Python source files in projects installed as editable will be reflected the next time an interpreter process is started.

Before installing the project in "editable" mode, [make sure to first activate your environment](#activate-a-virtual-environment),

```bash
# cd sdia-python
conda activate sdia-python
pip install -e .  # a (sdia-python) prefix must have appeared
```

See also

- <https://packaging.python.org/guides/distributing-packages-using-setuptools/#working-in-development-mode>
- <https://pip.pypa.io/en/latest/cli/pip_install/?highlight=editable#editable-installs>

## Integrated Development Environment - Visual Studio Code

[Visual Studio Code (VSCode)](https://code.visualstudio.com/) is recommended to ease your coding experience.

The [.vscode](./.vscode) directory contains a list of suggested extensions together with the corresponding settings.
You can place it at the root of your project workspace.

See also the [vscode-workflow](https://github.com/guilgautier/vscode-workflow) repository.

## Notebooks

[Jupyter](https://jupyter.org/) notebooks allow you to easily prototype code and showcase your project.

In order to automatically reflect modifications of the source files into your notebook, make sure your notebook has the following cell **and run it!**

```bash
%load_ext autoreload
%autoreload 2
```

**For example make this the top cell of your notebook.**

The [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) provides a full Jupyter notebook experience [within VSCode](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
