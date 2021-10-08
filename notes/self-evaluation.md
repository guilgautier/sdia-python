# Self-evaluation

Let's review your own work and the work of another duo.

Be fair, honest, factual and (try to) be objective.

At the end of this double reviewing process,

- discuss your reviews with the other duo
- **DO NOT COMMIT THIS FILE** except you really want to
- send this file to me by e-mail

Happy reviewing.

## Your duo

- name1-name2
- link to repository

### Code 0/5

- Are the `BoxWindow`, `UnitBoxWindow`, `BallWindow`, `UnitBallWindow` defined?
- Are the methods originally listed, now defined?
- Are there new methods defined? How are they used?
- How readable is the code?
- Are most of the operations "vectorized" using numpy? To which extent?
- How original is the code?

### Testing - 0/5

- Do the tests (all) pass?
- Are all functions/methods tested?
- Are the test readable?
- Are the tests meaningful?

### Documentation - 0/5

- Does the documentation build?
- Clarity/quality of the docstrings
  - Syntax
  - Consistency
  - Potential examples or doctests are provided
  - ...
- Does the documentation look nice? (this is more subjective)

### Packaging

See [packaging.md](.packaging.md)

[BONUS]

- Can the package be found on TestPyPI?
  - write the link here
- Does it install in a new environment?

## Review another duo

- name1-name2
- link to repository

0. Commit your last changes
1. Select an other duo (see the list below)
2. Copy paste the corresponding snippet of code (assuming you've followed the steps mentioned in [README.md](../README.md#get-the-project).
   - This will successively
     - create a new branch `name1-name2` from the initial commit with id `2240f62...` of the project
     - add a new remote `name1-name2` targeting the other duo's repository
     - pull their latest changes babe-fremerye will then be pulled from the associated remote
3. Start reviewing their work based on the same criteria you used to self-evaluate your duo

```language
# Aloïs Louis
git checkout -b babe-fremerye 2240f62
git branch
git log --oneline
git remote add babe-fremerye https://github.com/AloisBABE/sdia-python.git
git remote -v
git pull babe-fremerye main
git log --oneline

# Thomas Leo
git checkout -b besnier-beuque 2240f62
git branch
git log --oneline
git remote add besnier-beuque https://github.com/tbesnier/sdia-python.git
git remote -v
git pull besnier-beuque main
git log --oneline

# Hamza Oussama
git checkout -b jelloul-jourairi 2240f62
git branch
git log --oneline
git remote add jelloul-jourairi https://github.com/jouraOuss/sdia-python.git
git remote -v
git pull jelloul-jourairi main
git log --oneline

# Ayoub Zakaria
git checkout -b magga-oussalem 2240f62
git branch
git log --oneline
git remote add magga-oussalem https://github.com/02ayoub02/sdia-python.git
git remote -v
git pull magga-oussalem main
git log --oneline

# Benjamin Aurélien
git checkout -b cohen-orgiazzi 2240f62
git branch
git log --oneline
git remote add cohen-orgiazzi https://github.com/aurelienO/sdia-python.git>e
git remote -v
git pull cohen-orgiazzi main
git log --oneline

# Salim Amine
git checkout -b kabiri-ait_lemqeddem 2240f62
git branch
git log --oneline
git remote add kabiri-ait_lemqeddem https://github.com/KsalimK/sdia-python.git
git remote -v
git pull kabiri-ait_lemqeddem main
git log --oneline

# Aurian Georges
git checkout -b le_bellier-quelennec 2240f62
git branch
git log --oneline
git remote add le_bellier-quelennec https://github.com/gle-bellier/sdia-python.git
git remote -v
git pull le_bellier-quelennec main
git log --oneline

# Emilie Hadrien
git checkout -b salem-salem 2240f62
git branch
git log --oneline
git remote add salem-salem https://github.com/SnowHawkeye/sdia-python.git
git remote -v
git pull salem-salem main
git log --oneline

# Rémy Virgile
git checkout -b descarpentries-valiau 2240f62
git branch
git log --oneline
git remote add descarpentries-valiau https://github.com/VirgileValiau/sdia-python.git
git remote -v
git pull descarpentries-valiau main
git log --oneline

# Capucine Thomas
git checkout -b garcon-waldura 2240f62
git branch
git log --oneline
git remote add garcon-waldura https://github.com/CapucineGARCON/sdia-python.git
git remote -v
git pull garcon-waldura main
git log --oneline

# Anna Loan
git checkout -b marizy-sarazin 2240f62
git branch
git log --oneline
git remote add marizy-sarazin https://github.com/AnnaMarizy/sdia-python.git
git remote -v
git pull marizy-sarazin main
git log --oneline

# Justine Emilie
git checkout -b bourgain-yip 2240f62
git branch
git log --oneline
git remote add bourgain-yip https://github.com/JustineBrgn/sdia-python.git
git remote -v
git pull bourgain-yip main
git log --oneline
```
