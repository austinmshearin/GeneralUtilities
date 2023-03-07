"""
Strip plot graphing techniques for percept data
"""
# Standard Imports
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from typing import Union
import random
pd.set_option('mode.chained_assignment', None)

# Local imports
import utils.graph.color_palette as color_palette

# Environment Variables
# List of distinct colors to use for categorizing data
distinct_colors = color_palette.distinct_colors
# List of percepts in order
percept_list = ["fST", "fRS", "cCM", "cDF", "cDP", "cRX", "cYD", "tCO", "tPR", "aTK", "mTX", "mCO", "mRG", "uRO", "uCO"]


def sort_df(df: pd.DataFrame, groupby_col: str = "") -> pd.DataFrame:
    """
    Sorts the dataframe by percept type and group_by column so multi categorical x axis is in order

    Parameters
    ----------
    df: pd.DataFrame
        The percept dataframe
    groupby_col: str = ""
        The column that will create the multi categorical x axis

    Returns
    -------
    pd.DataFrame
        Percept dataframe after sorting
    """
    # Sort the percept type column by custom order in percept_list
    df["PerceptType"] = df["PerceptType"].astype("category")
    df["PerceptType"] = df["PerceptType"].cat.set_categories(percept_list)
    # Sort the dataframe by percepttype, groupby_col if used, and trial
    if groupby_col == "":
        df.sort_values(by=["PerceptType", "Trial"], inplace=True)
    else:
        df.sort_values(by=["PerceptType", groupby_col, "Trial"], inplace=True)
    # Convert the percept type column back to string column after sorting
    df["PerceptType"] = df["PerceptType"].astype(str)
    return df


def add_box(fig: go.Figure, df: pd.DataFrame, groupby_col: str = "") -> go.Figure:
    """
    Adds boxplots to the stripplot figure

    Parameters
    ----------
    fig: go.Figure
        The stripplot figure to add boxplots to
    df: pd.DataFrame
        The percept data to plot
    groupby_col: str = ""
        Plots multiple box plots per percept separated by group column values

    Returns
    -------
    go.Figure
        The stripplot figure with added boxplots
    """
    # No separating box plots into groups
    if groupby_col == "":
        fig.add_trace(
            go.Box(
                x=df["PerceptType"],
                y=df["PerceptValue"],
                fillcolor="rgba(255,255,255,0)",
                line={"color": "black", "width": 1},
                name="",
                boxpoints=False,
                hoveron="boxes",
                showlegend=False
            )
        )
    # Separating box plots into groups by columns values
    else:
        # Add unique boxplot for each group
        for group in df[groupby_col].unique():
            fig.add_trace(
                go.Box(
                    x=[df.loc[df[groupby_col] == group]["PerceptType"], df.loc[df[groupby_col] == group][groupby_col]],
                    y=df.loc[df[groupby_col] == group]["PerceptValue"],
                    fillcolor="rgba(255,255,255,0)",
                    line={"color": "black", "width": 1},
                    name=str(group),
                    boxpoints=False,
                    hoveron="boxes",
                    showlegend=False
                )
            )
    return fig


def add_points(fig: go.Figure, df: pd.DataFrame, groupby_col: str = "", colorby_col: str = "", legend_contents: list = None) -> go.Figure:
    """
    Adds markers to the stripplot figure

    Parameters
    ----------
    fig: go.Figure
        The stripplot figure to add points to
    df: pd.DataFrame
        The percept data to plot
    groupby_col: str = ""
        Plots points over multiple box plots per percept separated by column values
    colorby_col: str = ""
        Colors the points by column values
    legend_contents: list = None
        Keeps track of traces already recorded for the figure  
        if None, not to be recorded  

    Returns
    -------
    go.Figure or (go.Figure, legend_contents)
        The stripplot figure with added points and updated legend_contents if recorded
    """
    # No separating box plots into groups
    if groupby_col == "":
        # No coloring markers
        if colorby_col == "":
            fig.add_trace(
                go.Box(
                    x=df["PerceptType"],
                    y=df["PerceptValue"],
                    fillcolor="rgba(255,255,255,0)",
                    line={"width": 0},
                    marker={
                        "size": 5,
                        "color": "black",
                        "line": {"width": 1, "color": "black"}
                    },
                    name="",
                    boxpoints="all",
                    hoverinfo='skip',
                    pointpos=random.uniform(-0.8,0.8),
                    jitter=random.uniform(0.25,0.8),
                    showlegend=False
                )
            )
        # Coloring markers by column value
        else:
            # Each colorby_col gets separate boxplot with assigned color
            for marker_index, marker_group in enumerate(df[colorby_col].unique()):
                # Add marker to legend contents if not present
                if legend_contents is not None:
                    if marker_group not in legend_contents:
                        show_legend = True
                        legend_contents.append(marker_group)
                        marker_color = legend_contents.index(marker_group)
                    else:
                        show_legend = False
                        marker_color = legend_contents.index(marker_group)
                else:
                    show_legend = True
                    marker_color = marker_index
                # Add the boxplot points to the figure
                fig.add_trace(
                    go.Box(
                        x=df.loc[df[colorby_col] == marker_group]["PerceptType"],
                        y=df.loc[df[colorby_col] == marker_group]["PerceptValue"],
                        fillcolor="rgba(255,255,255,0)",
                        line={"width": 0},
                        marker={
                            "size": 5,
                            "color": distinct_colors[marker_color % 15],
                            "line": {"width": 1, "color": "black"}
                        },
                        name=str(marker_group)+" "*10,
                        boxpoints="all",
                        hoverinfo='skip',
                        pointpos=random.uniform(-0.8,0.8),
                        jitter=random.uniform(0.25,0.8),
                        showlegend=False,
                        legendgroup=str(marker_group)+" "*10
                    )
                )
                # Add a blank scatter to the figure and add to legend if it's not part of legend_contents
                fig.add_trace(
                    go.Scatter(
                        x=[None],
                        y=[None],
                        mode='markers',
                        marker={
                            "size": 5,
                            "color": distinct_colors[marker_color % 15],
                            "line": {"width": 1, "color": "black"}
                        },
                        name=str(marker_group)+" "*10,
                        showlegend=show_legend,
                        legendgroup=str(marker_group)+" "*10
                    )
                )
    # Separating box plots into groups by columns values
    else:
        # No coloring markers
        if colorby_col == "":
            fig.add_trace(
                go.Box(
                    x=[df["PerceptType"], df[groupby_col]],
                    y=df["PerceptValue"],
                    fillcolor="rgba(255,255,255,0)",
                    line={"width": 0},
                    marker={
                        "size": 5,
                        "color": "black",
                        "line": {"width": 1, "color": "black"}
                    },
                    name="",
                    boxpoints="all",
                    hoverinfo='skip',
                    pointpos=random.uniform(-0.8,0.8),
                    jitter=random.uniform(0.25,0.8),
                    showlegend=False
                )
            )
        # Coloring markers by column value
        else:
            # Each colorby_col gets separate boxplot with assigned color
            for marker_index, marker_group in enumerate(df[colorby_col].unique()):
                # Add marker to legend contents if not present
                if legend_contents is not None:
                    if marker_group not in legend_contents:
                        show_legend = True
                        legend_contents.append(marker_group)
                        marker_color = legend_contents.index(marker_group)
                    else:
                        show_legend = False
                        marker_color = legend_contents.index(marker_group)
                else:
                    show_legend = True
                    marker_color = marker_index
                # Add the boxplot points to the figure
                fig.add_trace(
                    go.Box(
                        x=[df.loc[df[colorby_col] == marker_group]["PerceptType"], df.loc[df[colorby_col] == marker_group][groupby_col]],
                        y=df.loc[df[colorby_col] == marker_group]["PerceptValue"],
                        fillcolor="rgba(255,255,255,0)",
                        line={"width": 0},
                        marker={
                            "size": 5,
                            "color": distinct_colors[marker_color % 15],
                            "line": {"width": 1, "color": "black"}
                        },
                        name=str(marker_group)+" "*10,
                        boxpoints="all",
                        hoverinfo='skip',
                        pointpos=random.uniform(-0.8,0.8),
                        jitter=random.uniform(0.25,0.8),
                        showlegend=False,
                        legendgroup=str(marker_group)+" "*10
                    )
                )
                # Add a blank scatter to the figure and add to legend if it's not part of legend_contents
                fig.add_trace(
                    go.Scatter(
                        x=[None],
                        y=[None],
                        mode='markers',
                        marker={
                            "size": 5,
                            "color": distinct_colors[marker_color % 15],
                            "line": {"width": 1, "color": "black"}
                        },
                        name=str(marker_group)+" "*10,
                        showlegend=show_legend,
                        legendgroup=str(marker_group)+" "*10
                    )
                )
    if legend_contents is None:
        return fig
    else:
        return (fig, legend_contents)


def add_perceptible(fig: go.Figure, df: pd.DataFrame, perceptible_groupby: Union[str, list] = []) -> go.Figure:
    """
    Highlights the percepts with perceptible differences

    Parameters
    ----------
    fig: go.Figure
        The stripplot figure to add the highlight regions to
    df: pd.DataFrame
        The percept data to plot
    perceptible_groupby: Union[str, list] = []
        Column/s in dataframe to groupby and average the percept values when determining human perceptibility  
        Defaults to each unique data point in each test  

    Returns
    -------
    go.Figure
        The stripplot figure with added highlighted regions
    """
    # Convert perceptible_groupby to list if necessary
    if type(perceptible_groupby) == str:
        perceptible_groupby = [perceptible_groupby]
    # Take the average of the data by perceptible_groupby column
    if perceptible_groupby == []:
        df_avg = df
    else:
        df_avg = df.groupby(perceptible_groupby + ["PerceptType"])["PerceptValue"].mean().reset_index()
    # Determine the percepts within the dataset
    percepts = list(df_avg["PerceptType"].unique())
    # Order the percepts by percept_list
    percepts = [percept for percept in percept_list if percept in percepts]
    # Determine the number of percepts
    num_percepts = len(percepts)
    # Calculate plotting x values by number of percepts available
    x_step = (1 / num_percepts) / 2
    x_refs = [(x / num_percepts) + x_step for x in range(num_percepts)]
    # Loop over each percept
    for percept_index, percept in enumerate(percepts):
        # Determine the percept range
        df_percept = df_avg.loc[df_avg["PerceptType"] == percept]
        percept_range = df_percept["PerceptValue"].max() - df_percept["PerceptValue"].min()
        # If perceptible range, add highlight shape to the figure
        if percept_range > 5:
            fig.add_shape(
                type="rect",
                xref="paper",
                yref="paper",
                x0=x_refs[percept_index]-x_step,
                x1=x_refs[percept_index]+x_step,
                y0=0,
                y1=1,
                fillcolor="blue",
                opacity=0.1,
                line_width=0
            )
    return fig


def add_perceptible_legend(fig: go.Figure) -> go.Figure:
    """
    Adds Perceptible reference to the legend

    Parameters
    ----------
    fig: go.Figure
        The stripplot figure to add the legend item

    Returns
    -------
    go.Figure
        The stripplot figure with added legend item
    """
    fig.add_trace(
        go.Box(
            x=[None],
            y=[None],
            fillcolor="blue",
            opacity=0.1,
            line={"width": 0},
            name="Human Perceptible",
            boxpoints=None,
            hoverinfo='skip',
            showlegend=True
        )
    )
    return fig


def app_percept_sep(fig: go.Figure, df: pd.DataFrame) -> go.Figure:
    """
    Adds vertical separators to the figure to separate percept types

    Parameters
    ----------
    fig: go.Figure
        The stripplot figure to add the vertical separators to
    df: pd.DataFrame
        The percept data in the plot

    Returns
    -------
    go.Figure
        The stripplot figure with vertical separators added
    """
    # Determine number of percepts in the stripplot
    num_percepts = len(list(df["PerceptType"].unique()))
    # Determine the placement of the vertical separators
    x_refs = [x_ref / num_percepts for x_ref in range(1,num_percepts)]
    for x_ref in x_refs:
        fig.add_shape(
            type="line",
            xref="paper",
            yref="paper",
            x0=x_ref,
            x1=x_ref,
            y0=0.05,
            y1=0.95,
            line_color="#555555",
            line_width=1
        )
    return fig


def plot(df: pd.DataFrame, groupby_col: str = "", colorby_col: str = "", perceptible: bool = True,
         perceptible_groupby: Union[str, list] = [], perceptible_legend: bool = True,
         legend_contents: list = None) -> go.Figure:
    """
    Plots all percept values vs percept type on stripplot boxplot

    Parameters
    ----------
    df: pd.DataFrame
        Every percept value should be on a separate row
    groupby_col: str = ""
        Column name to group boxplots by
    colorby_col: str = ""
        Column name to color markers by
    perceptible: bool = False
        Highlight percepts that have perceptible differences
    perceptible_groupby: Union[str, list] = []
        Column/s in dataframe to groupby and average the percept values when determining human perceptibility  
        Defaults to each unique data point in each test  
    perceptible_legend: bool = True
        Whether to add an item to the legend to denote perceptible percepts
    legend_contents: list = None
        Keeps track of traces already recorded for the figure  
        if None, not to be recorded  

    Returns
    -------
    go.Figure or (go.Figure, legend_contents)
        Plotly graph object figure and updated legend contents if recorded
    """
    # Sort the dataframe
    df = sort_df(df, groupby_col)
    # Generate the graph object figure
    fig = go.Figure()
    # Add boxplots to the figure
    fig = add_box(fig, df, groupby_col)
    # Add points to the figure
    if legend_contents is None:
        fig = add_points(fig, df, groupby_col, colorby_col)
    else:
        fig, legend_contents = add_points(fig, df, groupby_col, colorby_col, legend_contents)
    # Add axis titles
    if groupby_col == "":
        fig.update_layout(
            yaxis={"title": "Percept Value"},
            xaxis={"title": "Percept Type"}
        )
    else:
        fig.update_layout(
            yaxis={"title": "Percept Value"},
            xaxis={"title": "{} by Percept Type".format(groupby_col)}
        )
    # Add perceptible highlights to the figure
    if perceptible:
        fig = add_perceptible(fig, df, perceptible_groupby)
    # Adds item to legend to denote perceptible percepts
    if perceptible_legend:
        fig = add_perceptible_legend(fig)
    # Add vertical percept type separators to the figure
    fig = app_percept_sep(fig, df)
    # Format the x-axis
    fig.update_xaxes(
        fixedrange=True
    )
    # Format the figure y-axis
    fig.update_yaxes(
        range=[df["PerceptValue"].min() - 2, df["PerceptValue"].max() + 2],
        zeroline=True,
        zerolinewidth=0.1,
        zerolinecolor="#000000"
    )
    if legend_contents is None:
        return fig
    else:
        return (fig, legend_contents)


def multi_plot(df: pd.DataFrame, x_axis_col: str = "", y_axis_col: str = "", groupby_col: str = "", colorby_col: str = "",
               perceptible: bool = True, perceptible_groupby: Union[str, list] = []) -> go.Figure:
    """
    Plots the percept stripplot boxplot colored by group and subplotted by groups

    Parameters
    ----------
    df: pd.DataFrame
        Haptics dataframe
    x_axis_col: str = ""
        A column in the dataframe to separate subplots along the x-axis
    y_axis_col: str = ""
        A column in the dataframe to separate subplots along the y-axis
    groupby_col: str = ""
        A column to separate the data within the individual plots
    colorby_col: str = ""
        Column name to color markers by
    perceptible: bool = False
        Highlight percepts that have perceptible differences
    perceptible_groupby: Union[str, list] = []
        Column/s in dataframe to groupby and average the percept values when determining human perceptibility  
        Defaults to each unique data point in each test  

    Returns
    -------
    go.Figure
        Plotly figure
    """
    # Create the subplot object
    if x_axis_col == "":
        x_names = [""]
    else:
        x_names = list(df[x_axis_col].replace("", np.nan).dropna().unique())
    if y_axis_col == "":
        y_names = [""]
    else:
        y_names = list(df[y_axis_col].replace("", np.nan).dropna().unique())
    fig = make_subplots(
        rows=len(y_names),
        cols=len(x_names),
        x_title=x_axis_col,
        y_title=y_axis_col,
        row_titles=y_names,
        column_titles=x_names
    )
    # Generate list to monitor contents of the legend to prevent duplicate items
    legend_contents = []
    for col, x_name in enumerate(x_names):
        for row, y_name in enumerate(y_names):
            if x_name == "":
                x_where = np.array([True] * len(df))
            else:
                x_where = df[x_axis_col] == x_name
            if y_name == "":
                y_where = np.array([True] * len(df))
            else:
                y_where = df[y_axis_col] == y_name
            # Create dataframe with only data for particular row and column
            sub_df = df.loc[x_where & y_where]
            if groupby_col == "":
                # Create plot for specific row and column data
                sub_fig, legend_contents = plot(
                    df=sub_df,
                    colorby_col=colorby_col,
                    perceptible=perceptible,
                    perceptible_groupby=perceptible_groupby,
                    perceptible_legend=False,
                    legend_contents=legend_contents
                )
                # Extract the data from the single plot and put on multi plot
                for trace in sub_fig.data:
                    fig.append_trace(
                        trace,
                        row=row + 1,
                        col=col + 1
                    )
                for shape in sub_fig.layout.shapes:
                    if col == 0:
                        shape["xref"] = 'x domain'
                    else:
                        shape["xref"] = 'x{} domain'.format(col+1)
                    if row == 0:
                        shape["yref"] = 'y domain'
                    else:
                        shape["yref"] = 'y{} domain'.format(row+1)
                    fig.add_shape(
                        shape,
                        row=row+1,
                        col=col+1
                    )
            else:
                # Create plot for specific row and column data
                sub_fig, legend_contents = plot(
                    sub_df,
                    groupby_col=groupby_col,
                    colorby_col=colorby_col,
                    perceptible=perceptible,
                    perceptible_groupby=perceptible_groupby,
                    perceptible_legend=False,
                    legend_contents=legend_contents
                )
                # Extract the data from the single plot and put on multi plot
                for trace in sub_fig.data:
                    fig.append_trace(
                        trace,
                        row=row + 1,
                        col=col + 1
                    )
                for shape in sub_fig.layout.shapes:
                    if col == 0:
                        shape["xref"] = 'x domain'
                    else:
                        shape["xref"] = 'x{} domain'.format(col+1)
                    if row == 0:
                        shape["yref"] = 'y domain'
                    else:
                        shape["yref"] = 'y{} domain'.format(row+1)
                    fig.add_shape(
                        shape,
                        row=row+1,
                        col=col+1
                    )
    # Format the x-axis
    fig.update_xaxes(
        fixedrange=True
    )
    # Format the y-axis
    fig.update_yaxes(
        range=[df["PerceptValue"].min() - 2, df["PerceptValue"].max() + 2],
        matches="y",
        zeroline=True,
        zerolinewidth=0.1,
        zerolinecolor="#000000"
    )
    # Adds item to legend to denote perceptible percepts
    if perceptible:
        fig = add_perceptible_legend(fig)
    return fig
