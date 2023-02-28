from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

def get_data() -> pd.DataFrame:
    df = pd.read_excel("stable_coin_daily_2021-2022.xlsx", sheet_name=None)
    frames = []
    for key in df.keys():
        frames.append(df[key])

    df2 = pd.concat(frames)
    return df2

df = get_data()

assets_to_hide = []

fig = px.line(df, x="time", y="ReferenceRate", color="asset")

fig.for_each_trace(lambda trace: trace.update(visible="legendonly") 
                   if trace.name in assets_to_hide else ())

app.layout = html.Div(children=[
    html.H1(children='Stable Coin Daily Reference Rate 2021-2022'),

    html.Div(children='''
        Use the legend to toggle which assets to display.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=80)