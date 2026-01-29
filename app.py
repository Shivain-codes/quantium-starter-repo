from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# 1. Load data and fix the date type to prevent the TypeError
df = pd.read_csv('formatted_data.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by="date")

# 2. Create the line chart with axis labels
fig = px.line(
    df, 
    x="date", 
    y="sales", 
    title="Pink Morsel Sales Over Time",
    labels={'date': 'Date', 'sales': 'Total Sales ($)'}
)

# 3. Add the price increase marker (Jan 15, 2021)
fig.add_vline(x='2021-01-15', line_dash="dash", line_color="red")

# 4. App Layout
app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser", style={'textAlign': 'center'}),
    dcc.Graph(id='sales-graph', figure=fig)
])

# 5. Updated run command
if __name__ == '__main__':
    app.run(debug=True)