"""
Radar graphing techniques to apply to Toccare data

References
----------
https://plotly.com/python/polar-chart/
https://plotly.com/python/reference/scatterpolar/
https://plotly.com/python/reference/layout/polar/
https://plotly.com/python/reference/barpolar
"""
# Standard Imports
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from typing import Union
import math

# Local imports
import utils.graph.color_palette as color_palette

# List of distinct colors to use for categorizing data
distinct_colors = color_palette.distinct_colors

# List of percepts and their corresponding angles to use on a numerical radar graph
percept_list = ["fST", "fRS", "cCM", "cDF", "cDP", "cRX", "cYD", "tCO", "tPR", "aTK", "mTX", "mCO", "mRG", "uRO", "uCO"]
percept_angles = list(np.arange(0, 360, 360/len(percept_list)))
percept_dict = {percept: angle for percept, angle in zip(percept_list, percept_angles)}


def add_test(fig: go.Figure, df_test: pd.DataFrame, color: str, legend: bool = False, std: bool = False, **kwargs) -> go.Figure:
    """
    Add a Toccare test dataframe to the figure

    Parameters
    ----------
    fig: go.Figure
        The figure to add the data to  
    df_test: pd.DataFrame
        A dataframe which contains the percept data for a single test  
        Every value for each percept should be it's own row  
        The columns "PerceptType" and "PerceptValue" should exist for the percept name and percept data respectively  
    color: str
        color of the data for the test  
    legend: bool = False
        Whether to have the test data in the legend or not  
    std: bool = False
        Whether to graph a dashed line for 1 standard deviation  
        Only applies to data with all 15 dimensions  
    **kwargs
        All other keyword arguments will be passed to plotly.graph_objects.Scatterpolar  

    Returns
    -------
    go.Figure
        The figure with the added data

    Notes
    -----
    Common keyword arguments to pass in  
        name: name of test  
        line_color: color of the line  
    """
    # Performs a group by average so each perept type has an average value
    df_test_avg = df_test.groupby("PerceptType")["PerceptValue"].mean().reset_index()
    # Creates a list of percept average values sorted by the order of the percept_list
    plot_avg = []
    plot_theta = []
    for percept in percept_list:
        if percept in df_test_avg["PerceptType"].values:
            plot_theta.append(percept_dict[percept])
            plot_avg.append(df_test_avg.loc[df_test_avg["PerceptType"] == percept, "PerceptValue"].values[0])
    # If all 15 percept dimensions are present, create a line graph
    if len(plot_theta) == 15:
        # Appends the first value to the end so the radar line will close between the last and the first
        plot_avg = plot_avg + [plot_avg[0]]
        plot_theta = percept_angles + [percept_angles[0]]
        # Adds the data to the plotly.graph_objects.Figure
        fig.add_trace(
            go.Scatterpolar(
                r=plot_avg,  # Length from center of radar graph
                theta=plot_theta,  # Angle around radar graph
                mode='lines',  # Plotting mode: lines, markers, markers+lines
                line_width=1,  # Width of line in graph
                line_color=color,  # Color of the line
                showlegend=legend,  # Have data in legend or not
                **kwargs  # Other keyword arguments to format data
            )
        )
        # Plots a dashed line which represents one standard deviation away from the average
        if std:
            # Performs a group by standard deviation so each percept type has a standard deviation value
            df_test_std = df_test.groupby("PerceptType")["PerceptValue"].std().reset_index()
            # Creates a list of percept standard deviation values sorted by the order of the percept_list
            plot_std = [df_test_std.loc[df_test_std["PerceptType"] == percept, "PerceptValue"].values[0] for percept in percept_list]
            # Appends the first value to the end so the radar line will close between the actual last and the first
            plot_std = plot_std + [plot_std[0]]
            # Adds the one standard deviation below average data to the plotly.graph_objects.Figure
            fig.add_trace(
                go.Scatterpolar(
                    # Length from center of radar graph
                    r=[plot_avg[i] - plot_std[i] for i in range(len(plot_avg))],
                    theta=plot_theta,  # Angle around radar graph
                    mode='lines',  # Plotting mode: lines, markers, markers+lines
                    line_width=1,  # Width of line in graph
                    line_dash="dash",  # Line type: solid, dot, dash, longdash, dashdot, longdashdot
                    line_color=color,  # Color of the dashed line
                    showlegend=False,  # Whether data appears in legend or not
                    **kwargs  # Other keyword arguments to format data
                )
            )
            # Adds the one standard deviation above average data to the plotly.graph_objects.Figure
            fig.add_trace(
                go.Scatterpolar(
                    # Length from center of radar graph
                    r=[plot_avg[i] + plot_std[i] for i in range(len(plot_avg))],
                    theta=plot_theta,  # Angle around radar graph
                    mode='lines',  # Plotting mode: lines, markers, markers+lines
                    line_width=1,  # Width of line in graph
                    line_dash="dash",  # Line type: solid, dot, dash, longdash, dashdot, longdashdot
                    line_color=color,  # Color of the dashed line
                    showlegend=False,  # Whether data appears in legend or not
                    **kwargs  # Other keyword arguments to format data
                )
            )
    # Not all 15 dimensions are present in the data, add markers to represent data
    else:
        # Adds the data to the plotly.graph_objects.Figure
        fig.add_trace(
            go.Scatterpolar(
                r=plot_avg,  # Length from center of radar graph
                theta=plot_theta,  # Angle around radar graph
                mode='markers',  # Plotting mode: lines, markers, markers+lines
                marker_size=3,  # Width of line in graph
                marker_color=color,  # Color of the marker
                showlegend=legend,  # Have data in legend or not
                **kwargs  # Other keyword arguments to format data
            )
        )
    return fig


def add_dimensions(fig: go.Figure, radial_location: float) -> go.Figure:
    """
    Adds the curved rectangle dimension type data to the figure

    Parameters
    ----------
    fig: go.Figure
        The figure to add the data to
    radial_location: float
        The radial location for the dimension type shapes  
        Should be slightly further than the percept data so not overlapping

    Returns
    -------
    go.Figure
        The figure with the added dimension shapes
    """
    # Parameters to control the dimension type shapes
    shape_width = 0.5 * radial_location / 20  # Width of the curved rectangular shape
    dimension_types = {
        "Friction": {
            "Dimensions": ["fST", "fRS"],
            "Angle_Start": -6,
            "Angle_End": 30,
            "Color": "orange"
        },
        "Compliance": {
            "Dimensions": ["cCM", "cDF", "cDP", "cRX", "cYD"],
            "Angle_Start": 42,
            "Angle_End": 150,
            "Color": "brown"
        },
        "Thermal": {
            "Dimensions": ["tCO", "tPR"],
            "Angle_Start": 162,
            "Angle_End": 198,
            "Color": "green"
        },
        "Adhesive": {
            "Dimensions": ["aTK"],
            "Angle_Start": 210,
            "Angle_End": 222,
            "Color": "blue"
        },
        "Texture": {
            "Dimensions": ["mTX", "mCO", "mRG", "uRO", "uCO"],
            "Angle_Start": 234,
            "Angle_End": 342,
            "Color": "red"
        }
    }
    # Plot each dimension type shape
    for dimension_type, dimension_data in dimension_types.items():
        # Generate a list of angles that cover the distance of the shape in one direction
        dimension_angles = np.linspace(
            dimension_data["Angle_Start"],  # Angle start
            dimension_data["Angle_End"],  # Angle end
            # distance between is 5
            abs(dimension_data["Angle_Start"] - dimension_data["Angle_End"]) // 5).tolist()  # Convert numpy array to list
        # Generate list of thetas that create the curved rectangular shape
        # Goes one direction, then back, then closes the shape
        dimension_thetas = dimension_angles + dimension_angles[::-1] + [dimension_angles[0]]
        # Generate the radial list for the curved rectangular shape
        dimension_radar_lengths = [radial_location] * len(dimension_angles) \
            + [radial_location + shape_width] * len(dimension_angles) \
            + [radial_location]
        # Adds the curved rectangular shape to the graph
        fig.add_trace(
            go.Scatterpolar(
                r=dimension_radar_lengths,  # Length from center of radar graph
                theta=dimension_thetas,  # Angle around radar graph
                name=dimension_type,  # Name in the legend
                fill='toself',  # Fill the enclosed area within shape
                fillcolor=dimension_data["Color"],  # Sets color of the fill
                mode="lines",  # Plotting mode, but only want the fill
                line_width=0  # Set line width to zero so it doesn't show in figure
            )
        )
    return fig


def add_layout(fig: go.Figure, **kwargs) -> go.Figure:
    """
    Adds the custom layout to the figure

    Parameters
    ----------
    go.Figure
        The figure to add the custom layout to
    **kwargs
        Any additional keyword arguments to pass to graph_objects.Figure

    Returns
    -------
    go.Figure
        Figure with updated layout
    """
    fig.update_layout(
        polar_radialaxis_dtick=20,  # Tick location on the radial axis
        polar_radialaxis_gridcolor="#F0F0F0",  # Color of the radial axis grid
        polar_radialaxis_gridwidth=1,  # radial axis grid width
        # Setting 0 degrees to 90 degrees so fST is at the top
        polar_angularaxis_rotation=90,
        polar_angularaxis_gridcolor="#F0F0F0",  # Color of the angular axis grid
        polar_angularaxis_gridwidth=1,  # Angular axis grid width
        # Allows the angular text to be controlled by an array
        polar_angularaxis_tickmode="array",
        polar_angularaxis_tickvals=percept_angles,  # Tick text location
        polar_angularaxis_ticktext=percept_list,  # Tick text to display
        polar_bgcolor="#FFFFFF",  # Background color of the graph
        font_size=15,  # Universal font size
        margin={
            "l": 25,
            "r": 25,
            "b": 25,
            "t": 25,
            "pad": 1
        },
        legend={
            "x": 0.85
        },
        **kwargs
    )
    return fig


def add_perceptible(fig: go.Figure, df: pd.DataFrame, radial_length: float, groupby_cols: Union[str, list] = []) -> go.Figure:
    """
    Colors the percepts if they are perceptible to humans

    Parameters
    ----------
    fig: go.Figure
        The figure to add the data to
    df: pd.DataFrame
        The dataframe with the percept data used to make the original figure
    radial_length: float
        The radial length of the graph to fill the entire sector
    groupby_cols: Union[str, list] = []
        Columns in dataframe to groupby and average the percept values

    Returns
    -------
    go.Figure
        The figure with added perceptible regions colored
    """
    # Convert to list if necessary
    if type(groupby_cols) == str:
        groupby_cols = [groupby_cols]
    # Create list of thetas needed to plot to
    perceptible_theta = []
    # Take averages of dataframe using groupby_cols
    if groupby_cols == []:
        df_avg = df
    else:
        df_avg = df.groupby(groupby_cols + ["PerceptType"])["PerceptValue"].mean().reset_index()
    # Loop over each percept to determine if it's perceptible
    for percept_index, percept in enumerate(percept_list):
        df_percept = df_avg.loc[df_avg["PerceptType"] == percept]
        percept_range = df_percept["PerceptValue"].max() - df_percept["PerceptValue"].min()
        if percept_range > 5:
            perceptible_theta.append(percept_angles[percept_index])
    # Add perceptible regions to the figure
    if len(perceptible_theta) > 0:
        fig.add_trace(
            go.Barpolar(
                name="Human Perceptible",
                opacity=0.1,
                r=[radial_length] * len(perceptible_theta),
                theta=perceptible_theta,
                width=24,
                marker_color="blue",
                marker_line_width=0,
                hoverinfo="none"
            )
        )
    return fig


def plot(df: pd.DataFrame, groupby: str = None, perceptible: bool = True, std: bool = False, legend: bool = True,
         perceptible_groupby: Union[str, list] = []) -> go.Figure:
    """
    Plots all tests on the same radar graph with colors by groupby column in dataframe

    Parameters
    ----------
    data: pd.DataFrame
        A dataframe which contains the percept data  
        Every value for each percept for each test should be it's own row  
        The columns "PerceptType" and "PerceptValue" should exist for the percept name and percept data respectively  
    groupby: str
        Column name in the dataframe to use to group the data  
        Data from the same group will be the same color in the graph  
    perceptible: bool = True
        Whether to highlight the percepts that are perceptible to humans  
    std: bool = False
        Whether to graph a dashed line for 1 standard deviation  
        Only Available when all 15 dimensions are present in the data  
    legend: bool = True
        Whether to have data added to the legend or not  
    perceptible_groupby: Union[str, list] = []
        Column/s in dataframe to groupby and average the percept values when determining human perceptibility  
        Defaults to each unique data point in each test  

    Returns
    -------
    go.Figure
        Plotly graph object with grouped data

    Notes
    -----
    go.Figure.show()  
        Shows the plotly object  
    go.Figure.write_image(filepath)  
        Writes the image to a file  
    """
    # Initializing Plotly graph object
    fig = go.Figure()
    # If data is to be plotted in groups
    if groupby is not None:
        # Plot each group of data separately
        for group_index, group in enumerate(df[groupby].unique()):
            # Collect the data for the group
            df_group = df.loc[df[groupby] == group]
            # Flag so only one item gets added to the legend per group
            first = True
            # Plot every unique test in the group on the figure
            for test in df_group["TestName"].unique():
                # Collect all data for the particular test
                df_test = df_group.loc[df_group["TestName"] == test]
                if first:
                    # Add the test data to the figure
                    fig = add_test(
                        fig=fig,
                        df_test=df_test,
                        color=distinct_colors[group_index % 15],
                        std=std,
                        legend=legend,
                        name=group+"          ",
                        legendgroup=group
                    )
                    first = False
                else:
                    fig = add_test(
                        fig=fig,
                        df_test=df_test,
                        color=distinct_colors[group_index % 15],
                        std=std,
                        legend=False,
                        name=group+"          ",
                        legendgroup=group
                    )
    # If each test is plotted distinctly
    else:
        # Plot every unique test on the figure
        for test_index, test in enumerate(df["TestName"].unique()):
            # Collect all data for the particular test
            df_test = df.loc[df["TestName"] == test]
            # Add the test data to the figure
            fig = add_test(
                fig=fig,
                df_test=df_test,
                color=distinct_colors[test_index % 15],
                std=std,
                legend=legend,
                name=test+"          ",
                legendgroup=test
            )
    # Add the background dimension type data to the figure
    mean_max = df.groupby(["TestName", "PerceptType"])["PerceptValue"].mean().max()
    if std:
        std_max = df.groupby(["TestName", "PerceptType"])["PerceptValue"].std().max()
        # If standard deviation is not calculated, it will return np.nan
        if math.isnan(std_max):
            radial_location = ((mean_max // 20) + 1) * 20
        else:
            radial_location = (((mean_max + std_max) // 20) + 1) * 20
    else:
        radial_location = ((mean_max // 20) + 1) * 20
    fig = add_dimensions(fig, radial_location)
    # Highlight the perceptible percepts if desired
    if perceptible:
        fig = add_perceptible(fig, df, radial_location, perceptible_groupby)
    # Update the layout of the graph
    fig = add_layout(fig)
    return fig
