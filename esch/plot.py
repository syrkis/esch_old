# plot.py
#   eschews plots (minimally focused)
# by: Noah Syrkis

# imports
import plotly.graph_objects as go
import plotly.io as pio
import darkdetect

# globals
# Define a custom minimalistic theme based on the system theme
ink_color = 'black' if darkdetect.isLight() else 'white'
bg_color  = 'white' if darkdetect.isLight() else 'black'

axis = {
    'showgrid': False,
    'linecolor': ink_color,
    'linewidth': 1,
    'ticks': 'outside',
    'tickcolor': ink_color,
    'tickfont': {'size': 14, 'color': ink_color},
    'title_standoff': 15,
    'title_font': {'size': 18, 'color': ink_color},
    'showline': True,
    'mirror': True
}

minimalist_theme = {
    'layout': {
        'font': {'family': "Times New Roman, serif", 'size': 18, 'color': ink_color},
        'plot_bgcolor': bg_color,
        'paper_bgcolor': bg_color,
        'xaxis': axis,
        'yaxis': axis,
        'title': {'x': 0.5, 'xanchor': 'center', 'font': {'size': 22, 'color': ink_color}},
    }
}

# Apply the minimalist theme as default
pio.templates['minimalist'] = minimalist_theme
pio.templates.default = "minimalist"

# functions
def curves_fn(curves, info):
    fig = go.Figure()
    # Predefine a set of distinct line styles and colors
    line_styles = ['solid', 'dash', 'dot', 'dashdot']
    # colors = ['blue', 'red', 'green', 'purple']  # Change colors as per your minimalistic theme needs

    for i, curve in enumerate(curves):
        x_values = list(range(len(curve)))
        # Apply different line styles and colors based on index
        fig.add_trace(go.Scatter(
            x=x_values, y=curve, mode='lines',
            line=dict(width=2, color=ink_color, dash=line_styles[i])
        ))

    fig.update_layout(
        title={'text': info['title']}, 
        xaxis_title=info['xlab'], 
        yaxis_title=info['ylab']
    )
    return fig