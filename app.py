from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# Load and prepare data
df = pd.read_csv('formatted_data.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by="date")

# --- App Layout with CSS Styling ---
app.layout = html.Div(style={
    'backgroundColor': '#f9f9f9', 
    'fontFamily': 'Segoe UI, Tahoma, Geneva, Verdana, sans-serif',
    'padding': '40px'
}, children=[
    
    html.H1(
        "Pink Morsel Sales Visualiser", 
        style={'textAlign': 'center', 'color': '#2c3e50', 'marginBottom': '30px'}
    ),

    # Region Picker Section
    html.Div(style={'textAlign': 'center', 'marginBottom': '20px'}, children=[
        html.Label("Select Region:", style={'fontWeight': 'bold', 'marginRight': '10px'}),
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': 'all'}
            ],
            value='all', # Default value
            inline=True,
            style={'display': 'inline-block'}
        ),
    ]),

    # Graph Section
    html.Div(style={'backgroundColor': 'white', 'padding': '20px', 'borderRadius': '10px', 'boxShadow': '0px 4px 6px rgba(0,0,0,0.1)'}, children=[
        dcc.Graph(id='sales-graph')
    ])
])

# --- Interactivity Logic (Callback) ---
@app.callback(
    Output('sales-graph', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    fig = px.line(
        filtered_df, 
        x="date", 
        y="sales", 
        title=f"Sales Trend: {selected_region.capitalize() if selected_region != 'all' else 'All Regions'}",
        labels={'date': 'Date', 'sales': 'Total Sales ($)'},
        color_discrete_sequence=["#e67e22"] # A nice Pink/Orange color
    )
    
    fig.update_layout(plot_bgcolor='white')
    return fig

if __name__ == '__main__':
    app.run(debug=True)