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
    )
