# SDIA - Python

- [SDIA - Python](#sdia---python)
  - [Get the project](#get-the-project)

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
