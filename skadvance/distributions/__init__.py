import scipy.stats


def bernoulli(p=0.5):
    """
    Discrete distribution over {0,1} with p defining probability of 1.

    Useful for setting a prior on the usefulness of a True/False feature flag.

    For instance, assume that an `extra_trees` mode in LightGBM has a 10% change of being useful.
    """
    return scipy.stats.bernoulli(p)


def beta(a=0.5, b=0.5):
    """
    Continuous distribution on [0,1] interval.

    Useful for setting a prior on optimal values for a percent hyperparameter.

    For instance, assume that `l1_ratio` in LogisticRegression should favor ridge over lasso.

    Common shapes:
    a, b = 1, 1:        uniform
    a, b = 0.5, 0.5:    arcsine distribution; endpoints are most likely
    a, b = 2, 2:        midpoint is most likely
    a, b = 1, 3:        0 is most likely value; 1 is very unlikely
    a, b = 3, 1:        1 is most likely value; 0 is very unlikely
    """
    return scipy.stats.beta(a, b)


def triangle(
    low=0,
    mode=0.5,
    high=1,
):
    return scipy.stats.triang(loc=low, scale=high - low, c=mode)


def truncnorm(low=0, mean=0.5, high=1, std=0.5):
    return scipy.stats.truncnorm(loc=mean, scale=std, a=low, b=high)


def uniform(low=0, high=1):
    return scipy.stats.uniform(loc=low, scale=high - low)


def loguniform(low=0, high=1):
    return scipy.stats.reciprocal(a=low, b=high)


def int_uniform(low=0, high=1):
    return scipy.stats.randint(low, high)
