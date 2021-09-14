# Introduction

- [Introduction](#introduction)
  - [Command line basics](#command-line-basics)
    - [Exercise 1](#exercise-1)
    - [Exercise 2](#exercise-2)
  - [Version Control System - GIT and GitHub](#version-control-system---git-and-github)
    - [Install git](#install-git)
    - [Create a GitHub account](#create-a-github-account)
      - [Exercise 3](#exercise-3)
        - [Online](#online)
        - [On your machine](#on-your-machine)
        - [Back online](#back-online)
        - [Back to your machine](#back-to-your-machine)
    - [BONUSES](#bonuses)

## Command line basics

| Unix                       | Windows                            |
| :------------------------- | :--------------------------------- |
| `pwd`                      | `cd`                               |
| `ls`                       | `dir`                              |
| `mkdir folder_name`        | -                                  |
| `cd path`                  | -                                  |
| `cd or cd ~`               | `cd \`                             |
| `touch empty.txt`          | `echo $null > empty.txt`           |
| `echo hello > file.txt`    | -                                  |
| `cp current_path new_path` | - or `xcopy current_path new_path` |
| `mv current_path new_path` | - or `move current_path new_path`  |
| `rm path_to_file`          | - or `del path_to_file`            |
| `rm -r path_to_folder`     | `rmdir /s path_to_folder`          |

See also <https://www.lemoda.net/windows/windows2unix/windows2unix.html>

### Exercise 1

- When you open a terminal: what is your current directory?
- Check if your current directory is empty
- Navigate to the root using relative paths
- Navigate to your home from the root using relative paths

### Exercise 2

- Create a new folder called `sdia-cli`
- Create a file `hello.txt` in the `sdia-cli` folder containing only the `hello` string
- Duplicate the file with some other name, like `hi.txt`
- Move the `hi.txt` file into a new directory called `tmp`
- Duplicate the directory with some other name

## Version Control System - GIT and GitHub

### Install git

Check if git is already installed

```bash
git --version
```

If not, install it

- OSX
  - [install homebrew](https://brew.sh/), then
    - `brew install git`
- Linux
  - `sudo apt-get install git`
- Windows
  - [Download and install Git for Windows](https://git-scm.com/download/win)

Check if git installed properly

```bash
git --version
```

### Create a GitHub account

[GitHub](https://github.com/signup?source=login)

#### Exercise 3

First few steps with [git](https://git-scm.com/) and [GitHub](https://github.com), using the command line interface.

##### Online

- Create a new **blank** (no README, Licence, .gitignore files, etc.) GitHub repository called `sdia-git`.

##### On your machine

- Create a new folder called `sdia-git`
- Create a file `README.md` in the `sdia-git` folder containing at least the `# sdia-git` string at the top
- Run `git init` in the `sdia-git` folder
- Run successively and observe the output of the following commands
  - `git status`
  - `git add README.md`
  - `git status`
  - `git commit -m "first commit"`
  - `git status`
  - `git log`
  - `git branch -M main`
  - `git remote add origin https://github.com/<username>/sdia-git.git>`
  - `git push -u origin main`

##### Back online

- Delete your `sdia-git` repository
  - Settings
    - Danger Zone
      - Delete this repository
- Create a new `sdia-git` repository, but this time,
  - add README, Licence and .gitignore files.

##### Back to your machine

- Clone your new your `sdia-git` repository

  ```bash
  cd parent_directory_of_your_project
  git clone https://github.com/<your-username>/sdia-git.git
  ```

### BONUSES

- Customize the `README.md` file of your `sdia-git` repository with some [Mardown markup](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- Register for a [Student Developer Pack](https://education.github.com/pack)
