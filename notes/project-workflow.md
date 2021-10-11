# Important steps to follow when working on your project

1. Open your favorite shell
   - **Windows:** Open Anaconda Prompt (Windows key + Anaconda prompt)
   - **MacOS:** Open Terminal (CMD + Space + Terminal)

2. Navigate to your project folder
   - `cd path-to-your-project`, see also the "Command line basics" section in [command-line.md](./command-line.md#command-line-basics)

3. Activate your virtual environment
   - Conda, see also "Python Virtual environment with conda" section in [`anaconda-vscode.md`](./anaconda-vscode.md#python-virtual-environment-with-conda)
     - `conda deactivate  # deactivate current environment, most probably (base)`
     - `conda env list  # list available environment`
       - If your target environment is already available, activate it, e.g., for `sdia-python`
         - `conda activate sdia-python  # a (sdia-python) should appear`
       - Otherwise create a new environment and then activate it

4. Make sure your package is installed in editable mode
   - run `conda list` then find `your-package-name`, you should see something similar to

      ```bash
      your-package-name     version-number     dev_0     <develop>
      ```

   - otherwise see the section "Install the project in editable mode" in the main [README.md](../README.md#install-the-project-in-editable-mode) file.

5. Open your IDE
   - Visual Studio Code
      - See "Launch VSCode" section in [`anaconda-vscode.md`](./anaconda-vscode.md#launch-vscode)
      - Make sure your ["Python Interpreter"](https://code.visualstudio.com/docs/python/environments#_select-and-activate-an-environment) (CMD/CTRL + Maj + P -> Select interpreter) reflects your virtual environment
      - Make sure the ["Integrated Terminal"](https://code.visualstudio.com/docs/editor/integrated-terminal) (View -> Terminal) reflects your virtual environment, otherwise activate it as proposed mentioned above
         - **Windows:** make sure you use "Command prompt" and not "PowerShell"
         - **MacOS:** use preferably "zsh"

6. Run your tests, see the "Run tests" section in the [`tests-documentation.md`](./tests-documentation.md#run-tests)

   ```bash
   pytest
   ```

   - ideally all the tests should pass
   - otherwise fix them 🔩

7. Synchronize your project using git and GitHub
   - **Read `git` indications after running a command**
   - `git status`
     - ideally you would get messages like
       - "Your branch is up to date with 'origin/main'."
       - "nothing to commit, working tree clean", or
       - "nothing added to commit but untracked files present (use "git add" to track)"
     - otherwise
       - `git add/commit` your local changes
   - Get the latest modifs from the GitHub repositories of your choice (yours or your partner's)
     - `git pull remote-name main` and solve the potential merge conflicts ☺️
   - Get the latest material from the instructor
     - `git pull upstream main` and solve the potential merge conflicts ☺️

8. During your working session
   - write/update and run tests each time you create/modify a feature of your code
   - commit **OFTEN**
     - **when working with notebooks** first **CLEAR OUTPUTS**
     - save your files (CMD/CTRL + S), this should format them at the same time
     - `git status`
     - `git add path-to-file1 path-to-file2`
     - `git commit -m "Explicit commit message"`
   - synchronize the important changes with your partner when needed
     - first `git add/commit` (see above)
     - then `git push remote-name main`  and **read `git` indications after running a command**

9. At the end of your working session
   - run your tests, ideally they should all pass, see the "Run tests" section in the [tests-documentation.md](./tests-documentation.md#run-tests) file
   - build your documentation, see the "Generate the documentation" section in the [tests-documentation.md](./tests-documentation.md#generate-the-documentation) file
   - finally `git add/commit/push` (see above)

10. Close your computer, you're good to go, take a break!
