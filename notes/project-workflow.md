# Important steps to follow when working on your project

1. Open your favorite shell
   - **Windows:** Open Anaconda Prompt (Windows key + Anaconda prompt)
   - **MacOS:** Open Terminal (CMD + Space + Terminal)
2. Navigate to your project folder
   - `cd path-to-your-project`, see also "Command line basics" section in [text](./command_line.md)
3. Activate your virtual environment
   - Conda, see also "Python Virtual environment with conda" in [`anaconda-vscode.md`](./anaconda-vscode.md)
     - `conda deactivate  # deactivate current environment, most probably (base)`
     - `conda env list  # list availbale environment`
       - If your target environment is already available, activate it, e.g., for `sdia-python`
         - `conda activate sdia-python  # a (sdia-python) should appear`
       - Otherwise create a new environment and then activate it
4. Open your IDE
   - Visual Studio Code
      - "Launch VSCode" in [`anaconda-vscode.md`](./anaconda-vscode.md)
        - `code .`
      - Make sure your ["Python Interpreter"](https://code.visualstudio.com/docs/python/environments#_select-and-activate-an-environment) (CMD/CTRL + Maj + P -> Select interpreter) reflects your virtual environment
      - Make sure the ["Integrated Terminal"](https://code.visualstudio.com/docs/editor/integrated-terminal) (View -> Terminal) reflects your virtual environment, otherwise activate it as proposed in 3. above
         - **Windows:** make sure you use "Command prompt" and not "PowerShell"
         - **MacOS:** use preferably "zsh"
5. Synchronize your project with git and GitHub
   - **Read `git` indications after running a command**
   - `git status`, ideally you would get messages like
     - "Your branch is up to date with 'origin/main'."
     - "nothing to commit, working tree clean", or
     - "nothing added to commit but untracked files present (use "git add" to track)"
   - Get the latest modifs from the GitHub repositories of your choice (yours or your partner's)
     - `git pull remote-name main` and solve the potential merge conflicts ☺️
   - Get the latest material from the instructor
     - `git pull upstream main` and solve the potential merge conflicts ☺️
6. During your working session
   - commit **OFTEN**
     - **when working with notebooks** first **CLEAR OUTPUTS**
     - save your files (CMD/CTRL + S), this should format them at the same time
     - `git status`
     - `git add path-to-file1 path-to-file2`
     - `git commit -m "Explicit commit message"`
   - synchronize the important changes with your partner when needed
     - first `git add/commmit` (see above)
     - then `git push remote-name main`  and **read `git` indications after running a command**
7. At the end of your working session
   - commit and push your work as described in 6. above
8. Close your computer, you're good to go, take a break!
