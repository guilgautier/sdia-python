import numpy as np


def get_random_number_generator(seed):
    """Turn seed into a np.random.Generator instance."""
    return np.random.default_rng(seed)
