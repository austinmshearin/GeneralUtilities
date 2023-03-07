"""
Package contains common metrics calculations used for algorithm optimization
"""
# Standard Imports
import numpy as np

def rmse(prediction: np.array, target: np.array) -> float:
    """
    Returns root mean square error between prediction and target

    Parameters
    ----------
    prediction, target: np.array
        Discrete data points

    Returns
    -------
    float
        RMSE between prediction and target

    Examples
    --------
    >>> import numpy as np
    >>> pred = np.array([1, 2, 3])
    >>> targ = np.array([1.1, 2.1, 3.1])
    >>> rmse(pred, targ)
    0.10000000000000009
    """
    assert len(prediction) == len(target), "Length of arrays must be the same"
    if isinstance(prediction, list):
        prediction = np.asarray(prediction)
    if isinstance(target, list):
        target = np.asarray(target)
    return float(np.sqrt(((prediction - target) ** 2).mean()))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
