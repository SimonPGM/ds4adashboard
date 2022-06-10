import pandas as pd
import plotly.express as px
import numpy as np

def group_comparisons_bar(df, category, legend_title, title, ylabel):
    try:
        temp = df.melt(id_vars = [category])
        fig = px.bar(temp, x = category, y = "value", color= "variable", barmode="group",
        labels = {"value": ylabel, "variable": legend_title}, title = title)
        fig.update_layout(xaxis = dict(showticklabels = False))
        return fig
    except Exception:
        return None

def plot_cost(df, cost_column, eps_column, gender_column, diganostic_column, eps_value, days_column,
    diagnostic_value, gender_value, title):
    try:
        temp = df[(df[eps_column] == eps_value) & (df[gender_column] == gender_value) & (df[diganostic_column] == diagnostic_value)]
        total_days = temp[days_column].values[0]
        cost_per_day = temp[cost_column].values[0]
        x = np.arange(1, total_days + 1)
        y = np.cumsum(cost_per_day*x.copy())
        del temp, total_days
        to_plot = pd.DataFrame(x, y)
        fig = px.line(to_plot, x, y, labels=dict(x = "Día", y = "Costo acumulado"),
            title = f"{title}-Costo por diario promedio por paciente {np.ceil(cost_per_day)}")
        fig.add_bar(x = x, y = y, name = "Costo acumulado")
        return fig
    except Exception:
        return None
