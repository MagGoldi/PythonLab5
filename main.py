import torch
import torch.nn as nn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

import plotly.graph_objs as go
from plotly.offline import iplot

def plot_dataset(df, title):
    data = []
    
    value = go.Scatter(
        x=df.index,
        y=df.value,
        mode="lines",
        name="values",
        marker=dict(),
        text=df.index,
        line=dict(color="rgba(0,0,0, 0.3)"),
    )
    data.append(value)

    layout = dict(
        title=title,
        xaxis=dict(title="Date", ticklen=5, zeroline=False),
        yaxis=dict(title="Value", ticklen=5, zeroline=False),
    )

    fig = dict(data=data, layout=layout)
    iplot(fig)
    

device = "cpu"

df = pd.read_csv('C:\PYTHON\PythonLab5\dataset.csv')
df.columns = ['data', 'temp_day', 'wind', 'pressure_day', 'temp_even', 'pressure_even']  # 2

nan_value = float("NaN")                             # 3  ( null / None / Nan ) 
df.replace(" ", nan_value, inplace=True)
df = df.dropna()
df[['temp_day', "temp_even"]] = df[['temp_day', "temp_even"]].astype(int) 
print(df)

df = df.set_index(['data'])
df = df.rename(columns={'temp_day': 'value'})

df.index = pd.to_datetime(df.index)
if not df.index.is_monotonic_increasing:
    df = df.sort_index()
    
plot_dataset(df, title='PJM East (PJME) Region: estimated energy consumption in Megawatts (MW)')