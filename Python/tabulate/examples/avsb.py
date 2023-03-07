"""
A vs B table figure report
"""
# Standard Imports
import plotly.graph_objects as go
import pandas as pd
import scipy.stats as stats
pd.set_option('mode.chained_assignment', None)

# Environment Variables
# List of percepts in order
percept_list = ["fST", "fRS", "cCM", "cDF", "cDP", "cRX", "cYD", "tCO", "tPR", "aTK", "mTX", "mCO", "mRG", "uRO", "uCO"]


def plot(df_A: pd.DataFrame, df_B: pd.DataFrame) -> go.Figure:
    """
    Creates a table with summary data for A vs B test

    Parameters
    ----------
    df_A: pd.DataFrame
        The percept dataframe for group A
    df_B: pd.DataFrame
        The percept dataframe for group B

    Returns
    -------
    go.Figure
        The figure table with the results
    """
    # List of headers for the table
    headers = [
        "Percept", "Group A<br>Normality", "Group B<br>Normality", "Group A<br>Mean",
        "Group B<br>Mean", "Mean<br>Difference", "Statistically<br>Significant", "Human<br>Perceptible"
    ]
    # Initialize container for data
    values = [[] for _ in range(8)]
    # Initialize container for fill colors of cells
    fill_color = [[] for _ in range(8)]
    # Determine the percepts in both dataframes and sort by percept_list
    A_percepts = list(df_A["PerceptType"].unique())
    B_percepts = list(df_B["PerceptType"].unique())
    percepts = list(set(A_percepts).intersection(B_percepts))
    percepts = [percept for percept in percept_list if percept in percepts]
    for percept in percepts:
        # Add the percept to the data
        values[0].append(percept)
        fill_color[0].append('rgba(255,255,255,0)')
        # Determine group A normality
        _, p = stats.shapiro(df_A.loc[df_A["PerceptType"] == percept]["PerceptValue"].values)
        # Non-normal distribution
        if p <= 0.05:
            values[1].append("False")
            fill_color[1].append('rgba(255,165,0,0.2)')
        # Normal distribution
        else:
            values[1].append("True")
            fill_color[1].append('rgba(0,255,0,0.2)')
        # Determine group B normality
        _, p = stats.shapiro(df_B.loc[df_B["PerceptType"] == percept]["PerceptValue"].values)
        # Non-normal distribution
        if p <= 0.05:
            values[2].append("False")
            fill_color[2].append('rgba(255,165,0,0.2)')
        # Normal distribution
        else:
            values[2].append("True")
            fill_color[2].append('rgba(0,255,0,0.2)')
        # Group A mean value
        values[3].append(round(df_A.loc[df_A["PerceptType"] == percept]["PerceptValue"].mean(), 2))
        fill_color[3].append('rgba(255,255,255,0)')
        # Group B mean value
        values[4].append(round(df_B.loc[df_B["PerceptType"] == percept]["PerceptValue"].mean(), 2))
        fill_color[4].append('rgba(255,255,255,0)')
        # Mean difference
        values[5].append(round(abs(values[3][-1]-values[4][-1]), 2))
        if values[5][-1] > 5:
            fill_color[5].append('rgba(255,0,0,0.2)')
        else:
            fill_color[5].append('rgba(255,255,255,0)')
        # Welch T-test
        _, p = stats.ttest_ind(
            df_A.loc[df_A["PerceptType"] == percept]["PerceptValue"].values,
            df_B.loc[df_B["PerceptType"] == percept]["PerceptValue"].values,
            equal_var=False
        )
        if p <= 0.05:
            values[6].append("True")
            fill_color[6].append('rgba(0,255,0,0.2)')
        else:
            values[6].append("False")
            fill_color[6].append('rgba(255,165,0,0.2)')
        # Human perceptibility
        if values[6][-1] == "True":
            if values[5][-1] > 6:
                values[7].append("Yes")
                fill_color[7].append('rgba(255,0,255,0.2)')
            elif values[5][-1] > 5:
                values[7].append("Barely")
                fill_color[7].append('rgba(255,0,255,0.2)')
            elif values[5][-1] > 4:
                values[7].append("Almost")
                fill_color[7].append('rgba(255,255,255,0)')
            else:
                values[7].append("No")
                fill_color[7].append('rgba(255,255,255,0)')
        else:
            values[7].append("No")
            fill_color[7].append('rgba(255,255,255,0)')
    # Create the graph object figure table
    fig = go.Figure(
        data=[
            go.Table(
                header=dict(
                    values=headers,
                    line_color="black",
                    fill_color="white",
                    align="left",
                    font=dict(color="black", size=12)
                ),
                cells=dict(
                    values=values,
                    line_color="black",
                    fill_color=fill_color,
                    align="left",
                    font=dict(color="black", size=12)
                )
            )
        ]
    )
    fig.update_layout(
        height=600
    )
    return fig
