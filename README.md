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
  - [Jupyter Notebooks](#jupyter-notebooks)
    - [Launch a Jupyter notebook](#launch-a-jupyter-notebook)

Python course given to students enrolled in [Parcours DATA - Science des Données et Intelligence Artificielle (SDIA)](http://pierrechainais.ec-lille.fr/Centrale/Option_DAD/Accueil.html) managed by [Pierre Chainais](http://pierrechainais.ec-lille.fr/) at [Ecole Centrale de Lille](https://centralelille.fr/).

Some material is inspired and/or borrowed from courses previously given by:

- [Pierre-Antoine Thouvenin](https://pthouvenin.github.io/) at [Ecole Centrale de Lille - Data Science and Artificial Intelligence (SDIA)](http://pierrechainais.ec-lille.fr/Centrale/Option_DAD/Accueil.html), and
- [Guillermo Polito](https://guillep.github.io/) at [Université de Lille - M2 Data Science](https://www.univ-lille.fr/formations/fr-00020709.html).

## Get the project

It is suggested you [Fork](https://github.com/guilgautier/sdia-python/fork) the original repository.

> A [fork](https://docs.github.com/en/github/collaborating-with-pull-requests/working-with-forks/about-forks) is a copy of a repository that you manage.
> Forks let you make changes to a project without affecting the original repository.
> You can fetch updates from or submit changes to the original repository with [Pull Requests (PRs)](https://github.com/guilgautier/sdia-python/pulls).

1. [Fork](https://github.com/guilgautier/sdia-python/fork)
2. Clone: `git clone https://github.com/<your-username>/sdia-python.git`
3. [Create a remote](https://docs.github.com/en/github/collaborating-with-pull-requests/working-with-forks/configuring-a-remote-for-a-fork).

    ```bash
    cd sdia-python
    git remote -v # list the remotes ; an origin remote should be present
    git remote add upstream https://github.com/guilgautier/sdia-python.git
    git remote -v # remotes origin and upstream should be listed
    ```

This process allows you to link your local copy of `<your-username>/sdia-python` with the original repository `guilgautier/sdia-python`, so that you can fetch updates from it, e.g., corrections, new course material, etc.

[![git remotes](https://www.tomasbeuzen.com/post/git-fork-branch-pull/featured_hud478d74d48d19bfd1c1c03fc398c8033_312322_720x0_resize_lanczos_2.png)](https://www.tomasbeuzen.com/post/git-fork-branch-pull/)

For example, at the beginning of a practical session, to get the latest course material

```bash
git checkout main # select your main branch
git pull upstream main # fetch and merge commits from guilgautier/sdia-python
```

Note: Merge conflicts may occur 😏. We'll see how to handle this **very** common situation.

## Set up your working environment

We will use [`conda`](https://conda.io/projects/conda/en/latest/index.html) to manage Python packages and virtual environments

### Virtual environment

See also [notes/anaconda-vscode.md](./notes/anaconda-vscode.md)

#### Create a virtual environment

> A [virtual environment](https://docs.python.org/3/tutorial/venv.html) is a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages.

It is always good practice to work in a virtual environment, isolated from your other Python projects.

The [environment.yml](./environment.yml) file contains the list of the main packages that will be installed when creating the environment

```bash
cd sdia-python
# conda env list
conda env create -f environment.yml
```

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
import sdia_python.lab1
from sdia_python.lab1.xxx import yyy
```

> You can [install a project in "editable" or "develop" mode](https://packaging.python.org/guides/distributing-packages-using-setuptools/#working-in-development-mode) while you’re working on it.
> When installed as editable, a project can be edited in-place without reinstallation:
> changes to Python source files in projects installed as editable will be reflected the next time an interpreter process is started.

Before installing the project in "editable" mode, [make sure to first activate your environment](#activate-a-virtual-environment),

```bash
# cd sdia-python
conda activate sdia-python # a (sdia-python) prefix should appear
pip install -e .
```

See also

- <https://packaging.python.org/guides/distributing-packages-using-setuptools/#working-in-development-mode>
- <https://pip.pypa.io/en/latest/cli/pip_install/?highlight=editable#editable-installs>

## Integrated Development Environment - Visual Studio Code

[Visual Studio Code (VSCode)](https://code.visualstudio.com/) is recommended to ease your coding experience.

See the [notes/anaconda-vscode.md](./notes/anaconda-vscode.md) file.

## Jupyter Notebooks

[Jupyter](https://jupyter.org/) notebooks allow you to easily prototype code and showcase your project, see [`notebooks/`](./notebooks/) folder.

In order to automatically reflect modifications of the source files (located in [`src/`](./src/)) into your notebook, make sure your notebook has the following cell **and run it!**

```bash
%load_ext autoreload
%autoreload 2
```

**For example make this the top cell of your notebook.**

### Launch a Jupyter notebook

- From the command line

  ```bash
  # cd sdia-python/notebooks
  # activate sdia-python
  jupyter notebook
  ```

- Within VSCode
  - The [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) provides a full [Jupyter notebook experience within VSCode](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
    - Simply open a `.ipynb` file located in [`notebooks/`](./notebooks/)
