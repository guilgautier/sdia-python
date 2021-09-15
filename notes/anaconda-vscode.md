# Define your project environments

- [Define your project environments](#define-your-project-environments)
  - [Python Virtual environment with conda](#python-virtual-environment-with-conda)
    - [Exercise 1](#exercise-1)
  - [Integrated Development Environment](#integrated-development-environment)
    - [Launch VSCode from the command line](#launch-vscode-from-the-command-line)
    - [Per project configuration](#per-project-configuration)
    - [Extensions](#extensions)
      - [Exercise 2](#exercise-2)
    - [Settings](#settings)
      - [Exercise 3](#exercise-3)
    - [Snippets](#snippets)
      - [Exercise 4](#exercise-4)

## Python Virtual environment with conda

> A [virtual environment](https://docs.python.org/3/tutorial/venv.html) is a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages.

It is always good practice to work in a virtual environment, isolated from your other Python projects.

In this course, we will use [`conda`](https://docs.conda.io/projects/conda/en/latest/index.html), both as

- an [environment manager](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#)
- a [package manager](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html).

See also the [conda cheat sheet](https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html).

### Exercise 1

- Read the [Getting Started section of the conda documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html)
<https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html>
- Display the list of conda environments currently available on your machine

- For the `base` environment
  - list the installed packages
  - what were the different channels used to install the different packages

- Create a conda environment called `myenv` with Python 3.8.2
  - install `numpy`
  - install `matplotlib` using `pip`
  - list the installed packages
  - export the environment to a cross-platform `myenv.yml` file
  - delete the environment `myenv`

- Recreate the conda environment `myenv` from the previous `myenv.yml` file
  - update the Python version to its latest version.
  - install `scipy` using the `conda-forge` channel
  - export the environment to a cross-platform `myenv2.yml` file

## Integrated Development Environment

[Visual Studio Code (VSCode)](https://code.visualstudio.com/) is recommended to ease your coding experience.

**Important:** Use the [command palette](https://code.visualstudio.com/docs/getstarted/tips-and-tricks#_command-palette) ( `CMD/CRTL + Maj + P` ).

See also

- [VSCode setup documentation](https://code.visualstudio.com/docs/setup/setup-overview)
- [guilgautier/vscode-workflow](https://github.com/guilgautier/vscode-workflow) repository

**Tip:** You may also consider [synchronizing your settings](https://code.visualstudio.com/docs/editor/settings-sync), in order to keep the same setup each time you log in VS Code (even from a different machine for example).

### Launch VSCode from the command line

```bash
code . # open VSCode and define workspace from current directory
code README.md  # open README.md in VSCode
```

See also

- [VSCode command line](https://code.visualstudio.com/docs/getstarted/tips-and-tricks#_command-line)
- [code is not recognized as an internal or external command](https://code.visualstudio.com/docs/editor/command-line#_code-is-not-recognized-as-an-internal-or-external-command)

### Per project configuration

The [.vscode](./.vscode) directory, placed at the root of your project workspace, contains a list of suggested extensions together with the corresponding settings, code snippets, etc.
You can share the [.vscode](./.vscode) directory with your collaborator, e.g., using git/GitHub, to make sure you have the same setup.

Note: This configuration only applies in the current workspace and has precedence over global user settings, see also [Settings](#settings) and [Snippets](#snippets).

### Extensions

All registered extensions are available on [VSCode's Marketplace](https://marketplace.visualstudio.com/vscode).
Extensions can also be installed locally from your VSCode window, see the [documentation](https://code.visualstudio.com/docs/editor/extension-marketplace).

The [.vscode/extensions.json](../.vscode/extensions.json) file contains a list of suggested extensions that will *greatly* simplify your coding workflow.

#### Exercise 2

- Install the extensions listed in [.vscode/extensions.json](../.vscode/extensions.json)
- Activate/Deactivate the `Multiline Comments` setting of the `Better Comments` extension

### Settings

> [VSCode settings](https://code.visualstudio.com/docs/getstarted/settings) You can configure Visual Studio Code to your liking through its various settings. Nearly every part of VS Code's editor, user interface, and functional behavior has options you can modify.

To do so, you can either define settings

- Globally: Open the Command Palette ( `CMD/CRTL + Maj + P` ) and type either
  - `Open User Settings`, or
  - `Open Settings (JSON)`,
- Per project: see [settings.settings](../.vscode/workspace.code-snippets).

See also [guilgautier/vscode-workflow](https://github.com/guilgautier/vscode-workflow) repository.

#### Exercise 3

- Change the location of VSCode the sidebar left <-> right.

### Snippets

> [Code snippets](https://code.visualstudio.com/docs/editor/userdefinedsnippets) are templates that make it easier to enter repeating code patterns, such as loops or conditional-statements.

Many language-specific [extensions](#extensions) already provide some useful snippets.
While some of them exactly match your needs, some others might be missing or you may not remember how to trigger them.

For these reasons you may create your own snippets to increase your productivity.
To do so, you can either define snippets

- Globally: Open the Command Palette ( `CMD/CRTL + Maj + P` ) and type `Configure User Snippets` and choose to create
  - language-specific snippets,
  - generic snippets that can be triggered in different scopes.
- Per project: see [workspace.code-snippets](../.vscode/workspace.code-snippets)

See also [guilgautier/vscode-workflow](https://github.com/guilgautier/vscode-workflow) repository.

#### Exercise 4

- Create your own `mygithub` snippet and make it available only in Markdown (`.md`) files.
- Create an `forenum` Python snippet, that displays when triggered in Python (`.py`) files

  ```python
  for idx, val in enumerate(values):
      print(idx, val)
  ```
