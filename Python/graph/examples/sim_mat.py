"""
Graphing utilities for creating similarity matrices/heatmaps
"""
# Standard Imports
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from typing import Union

# Local Imports
import utils.stats as stats


class NonUniformPerceptTypes(Exception):
    """
    Raised when the percept types are not shared between all tests
    """
    pass


def all(df: pd.DataFrame, highlight: Union[None, str, list] = None) -> go.Figure:
    """
    Heatmap similarity matrix between tests in the dataset

    Parameters
    ----------
    df: pd.DataFrame
        Dataset to use to calculate the similarity matrix  
        Should contain columns: TestName, PerceptType, PerceptValue  
        Each value for each percept for each test should be a unique row
    highlight: Union[None, str, list] = None
        Tests to highlight in similarity matrix  
        Can be single test name or list of tests  
        These will be the tests on the y-axis

    Returns
    -------
    go.Figure
        Greyscale heatmap of the similarity matrix
    """
    # List of unique tests
    x_tests = list(df["TestName"].unique())
    # Separate the x- and y-axis tests labels
    if highlight is None:
        y_tests = x_tests
    elif type(highlight) == str:
        y_tests = [highlight]
    elif type(highlight) == list:
        y_tests = highlight
    else:
        raise Exception("Received invalid argument for highlight: {}".format(highlight))
    # List of unique percepts
    percepts = df["PerceptType"].unique()
    # Check that every test has the same percept types available
    for test in x_tests:
        df_test = df[df["TestName"] == test]
        for percept in percepts:
            if percept not in df_test["PerceptType"].values:
                raise NonUniformPerceptTypes
    # Initialize similarity matrix with all ones
    sim_mat = np.ones((len(y_tests), len(x_tests)))
    # Calculate the average percept value for each percept per each test
    df_avg = df.groupby(["TestName", "PerceptType"])["PerceptValue"].mean()
    # Calculate the standard deviation for each percept per each test
    df_std = df.groupby(["TestName", "PerceptType"])["PerceptValue"].std()
    # Loop over each row of the similarity matrix
    for row_index, row in enumerate(y_tests):
        # Loop over each column of the similarity matrix
        for col_index, col in enumerate(x_tests):
            # No calculations needed when comparing to self
            if row != col:
                # Container for holding means and standard deviations
                u1 = []
                u2 = []
                s1 = []
                s2 = []
                # Loop over each percept
                for percept in percepts:
                    u1.append(df_avg[row][percept])
                    u2.append(df_avg[col][percept])
                    s1.append(df_std[row][percept])
                    s2.append(df_std[col][percept])
                # Assign distance value to similarity matrix
                sim_mat[row_index][col_index] = stats.distribution_distance(u1, s1, u2, s2)
    return plot(x_tests, y_tests, sim_mat)


def most_similar(df: pd.DataFrame, target: str, number_similar: int = 10) -> go.Figure:
    """
    One dimensional heatmap similarity matrix between target test and most similar tests in the dataset

    Parameters
    ----------
    df: pd.DataFrame
        Dataset to use to calculate the similarity matrix  
        Should contain columns: TestName, PerceptType, PerceptValue  
        Each value for each percept for each test should be a unique row
    target: str
        The target test to find similar data to
    number_similar: int = 10
        The number of closest tests to return

    Returns
    -------
    go.Figure
        Greyscale heatmap of the similarity matrix
    """
    # The only y test is the target
    y_tests = [target]
    # Container to store x tests
    x_tests = []
    # List of tests in the dataset
    tests = df["TestName"].unique()
    # List of unique percepts
    percepts = df["PerceptType"].unique()
    # Check that every test has the same percept types available
    for test in tests:
        df_test = df[df["TestName"] == test]
        for percept in percepts:
            if percept not in df_test["PerceptType"].values:
                raise NonUniformPerceptTypes
    # Initialize similarity matrix with all ones
    if len(tests) - 1 < number_similar:
        sim_mat = np.ones((1, len(tests) - 1))
    else:
        sim_mat = np.ones((1, number_similar))
    # Calculate the average percept value for each percept per each test
    df_avg = df.groupby(["TestName", "PerceptType"])["PerceptValue"].mean()
    # Calculate the standard deviation for each percept per each test
    df_std = df.groupby(["TestName", "PerceptType"])["PerceptValue"].std()
    # Container to hold the distance data
    distances = {}
    # Determine target means and standard deviations
    u1 = []
    s1 = []
    for percept in percepts:
        u1.append(df_avg[target][percept])
        s1.append(df_std[target][percept])
    # Loop over each test and calculate the distance
    for test in tests:
        if test != target:
            u2 = []
            s2 = []
            for percept in percepts:
                u2.append(df_avg[test][percept])
                s2.append(df_std[test][percept])
            distances[test] = stats.distribution_distance(u1, s1, u2, s2)
    # Loop through distances in order or closest first
    for test, distance in sorted(distances.items(), key=lambda item: item[1], reverse=True):
        x_tests.append(test)
        sim_mat[0, len(x_tests) - 1] = distance
        if len(x_tests) == len(sim_mat[0, :]):
            return plot(x_tests, y_tests, sim_mat)


def plot(x_tests, y_tests, sim_mat) -> go.Figure:
    """
    Creates the heatmap plot from the similarity matrix data

    Parameters
    ----------
    x_tests: list [str]
        The labels for the x axis
    y_tests: list [str]
        The labels for the y axis
    sim_mat: np.array
        The similarity matrix data

    Returns
    -------
    go.Figure
        Greyscale heatmap of the similarity matrix
    """
    # Initialize plotly figure
    fig = go.Figure()
    # Add the heatmap to the plotly figure
    fig.add_traces(
        go.Heatmap(
            z=sim_mat,
            x=x_tests,
            y=y_tests,
            text=sim_mat,
            texttemplate="%{text}",
            colorscale="greys",
            reversescale=False,
            zmin=0,
            zmax=1
        )
    )
    fig.update_yaxes(autorange="reversed")
    return fig
