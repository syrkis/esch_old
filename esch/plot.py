# plot.py
#   eschews plots (minimally focused)
# by: Noah Syrkis

# imports
import plotly.express as px
import plotly.io as pio

# globals
# Define a custom minimalistic theme

axis = {
    'showgrid': False,
    'linecolor': 'black',
    'linewidth': 1,
    'ticks': 'outside',
    'tickfont': {'size': 14},
    'tickwidth': 1,
    'showline': True,
    'mirror': True,
    'title_standoff': 50  # Adjust this value to move the axis title further away
}

minimalist_theme = {
    'layout': {
        'font': {'family': "Times New Roman, serif", 'size': 18},
        'plot_bgcolor': 'white', 'paper_bgcolor': 'white',
        'xaxis': axis, 'yaxis': axis
    }
}

# Apply the minimalist theme as default
pio.templates['minimalist'] = minimalist_theme
pio.templates.default = "minimalist"

# plot loss curve
def train_curve(losses):
    fig = px.line(losses, template="minimalist")
    # Additional customizations for a more old-school, minimalist look
    fig.update_traces(line=dict(width=2, color='black'))  # Thicker, black line for the graph
    return fig
