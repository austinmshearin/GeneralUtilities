"""
Statistic operations
"""
# Standard Imports
import math
import numpy as np


def distribution_distance(u1: list, s1: list, u2: list, s2: list) -> float:
    """
    Calculates the geometric mean of Bhattacharyya Distance between two samples of multiple features

    Parameters
    ----------
    u1: list [float]
        The means for each feature within sample 1
    s1: list [float]
        The standard deviation for each feature within sample 1
    u2: list [float]
        The means for each feature within sample 2
    s2: list [float]
        The standard deviations for each feature within sample 2

    Returns
    -------
    float
        The similarity between two probability distributions

    Notes
    -----
    Equation
    S_{ij}=\left(\prod\limits_{p=1}^{p}\sqrt{\frac{2\sigma_{i,p}\sigma_{j,p}}{\sigma_{i,p}^{2}+\sigma_{j,p}^{2}}}e^{-\frac{\left(\mu_{i,p}-\mu_{j,p}\right)^{2}}{4\left(\sigma_{i,p}^{2}+\sigma_{j,p}^{2}\right)}}\right)^{\frac{1}{P}}
    Latex Viewer
    https://latex.codecogs.com/eqneditor/editor.php
    """
    # Check that all variables are the same length
    assert (len(u1) == len(s1)) & (len(u1) == len(u2)) & (len(u2) == len(s2))
    product_list = []
    # Loop over each feature to calculate the inner product term
    for feature in range(len(u1)):
        # 0 standard deviation will cause the calculation to be undefined
        if s1[feature] == 0:
            s1[feature] = 1e-15
        if s2[feature] == 0:
            s2[feature] = 1e-15
        # Calculate the distance between two feature distributions
        product_list.append(
            np.sqrt(
                (2 * s1[feature] * s2[feature])
                / ((s1[feature])**2 + (s2[feature])**2)
            )
            * np.exp(
                -((u1[feature] - u2[feature])**2)
                / (4 * ((s1[feature])**2 + (s2[feature])**2))
            )
        )
    # Take the product and root
    dist = round(np.prod(product_list)**(1/len(u1)), 2)
    if math.isnan(dist):
        return 0
    else:
        return dist
