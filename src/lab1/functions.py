def is_unique(x):
    M = []
    for value in x:
        if value not in M:
            M.append(value)
    return len(M) == len(x)
