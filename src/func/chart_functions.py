import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def bar_chart(df: pd.DataFrame, xaxis: str, yaxis: str, title: str) -> go.Figure:
    """
    Returns Plotly Bar chart.
        :df - Pandas DataFrame
        :xaxis - column name for x axis
        :yaxis - column name for y axis
        :title - title of the chart
    """
    return px.bar(
        data_frame=df,
        x=xaxis,
        y=yaxis,
        text_auto=True,
        title=title,
        width=1200,
        height=300,
        color_discrete_sequence=["#e6cea0"],
    ).update_layout(template="plotly_white")


def histogram_chart(
    df: pd.DataFrame, xaxis: str, title: str, color: str = None, bins: int = None
) -> go.Figure:
    """
    Return Plotly Histogram chart.
        :df - Pandas DataFrame
        :xaxis - column for x axis
        :title - title for chart
        :bins - default value are None, change to number
    """
    return px.histogram(
        data_frame=df,
        x=xaxis,
        title=title,
        width=1200,
        height=500,
        color_discrete_sequence=["#e6cea0"],
        nbins=bins,
    ).update_layout(template="plotly_white")


def histogram_chart_color(
    df: pd.DataFrame, xaxis: str, title: str, color: str = None, bins: int = None
) -> go.Figure:
    """
    Return Plotly Histogram chart.
        :df - Pandas DataFrame
        :xaxis - column for x axis
        :title - title for chart
        :color - default None, change if want show by type
        :bins - default value are None, change to number
    """
    return px.histogram(
        data_frame=df,
        x=xaxis,
        title=title,
        width=1200,
        height=500,
        color=color,
        color_discrete_sequence=["#095786", "#db4646", "#e6cea0"],
        nbins=bins,
    ).update_layout(template="plotly_white")
