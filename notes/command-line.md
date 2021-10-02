# Introduction

- [Introduction](#introduction)
  - [Command line basics](#command-line-basics)
    - [Exercise 1](#exercise-1)
    - [Exercise 2](#exercise-2)

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
