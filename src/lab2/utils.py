import numpy as np


def get_random_number_generator(seed):
    """Turn seed into a np.random.Generator instance."""
    return np.random.default_rng(seed)


rng = get_random_number_generator(None)
bounds = np.array([0.5, 0.5])
print((1 - rng.random()) * bounds[0] + rng.random() * bounds[1])
