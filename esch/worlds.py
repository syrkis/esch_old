# worlds.py
#   plots simulated worlds (SORTSOL and C2SIM)
# by: Noah Syrkis

# imports
import jax.numpy as jnp
import matplotlib.pyplot as plt
import imageio_ffmpeg  # Make sure this is installed
from matplotlib import rcParams
import numpy as np
import imageio
import darkdetect
from tqdm import tqdm

# globals
rcParams['font.family'] = 'monospace'
rcParams['font.monospace'] = 'Fira Code'
bg = 'black' if darkdetect.isDark() else 'white'
ink = 'black' if bg == 'white' else 'white'

# functions
def worlds_fn(seqs, info):
    grid_size = (2, 3)  # For a 4x4 grid
    figsize = (17.92, 12)  # Adjusted size of the figure


    # Prepare a list to hold all frames (as NumPy arrays)
    frames = []
    n = len(seqs)
    for i in tqdm(range(n)):
        key, state, action = seqs[i]
        title = f"agent : {info['agent']}        step : {str(i//8).zfill(len(str(n-1)))}        scenario : {info['scenario']}"
        fig, axes = plt.subplots(*grid_size, figsize=figsize, facecolor=bg, dpi=100)  # Set background to black
        plt.subplots_adjust(left=0.05, bottom=0.05, right=0.95, top=0.95, wspace=0.3, hspace=0.3)
        fig.text(0.01, 0.5, title, va='center', rotation='vertical', fontsize=24, color=ink)
        for j, ax in enumerate(axes.flatten()):
            plot_ax(ax, state, j, bg)
        fig.canvas.draw()
        data = np.frombuffer(fig.canvas.buffer_rgba(), dtype=np.uint8)
        data = data.reshape(fig.canvas.get_width_height()[::-1] + (4,))[:, :, :3]
        frames.append(data)
        if i == n - 1:
            plt.savefig(f'docs/figs/worlds_{bg}.jpg', dpi=200)
        plt.close(fig)

    mp4_path = f'docs/figs/worlds_{bg}.mp4'
    imageio.mimsave(mp4_path, frames, fps=24)



def plot_ax(ax, state, j, bg):
    tick_interval = 4
    marker_styles = ['o', 's', 'D', '^', 'v', '>']  # Add or change shapes as needed
    
    # Convert JAX arrays to NumPy arrays for operations not supported by JAX, like 'unique'
    teams = np.array(state.unit_teams[j, :]).astype(int)
    types = np.array(state.unit_types[j, :]).astype(int)
    pos   = np.array(state.unit_positions[j, :])
    
    unique_teams = np.unique(teams)
    unique_types = np.unique(types)
    
    for team in unique_teams:
        for unit_type in unique_types:
            # Find indices where the current team and unit type are located
            indices = (teams == team) & (types == unit_type)
            # Extract x and y coordinates for these indices
            x, y = pos[indices, 0], pos[indices, 1]

            fill_style = 'full' if team == 0 else 'none'  # Assuming team 0 is filled, team 1 is not
            marker = marker_styles[unit_type % len(marker_styles)]  # Select marker style based on unit type
            
            # Plot each unit with specific marker and fill style
            ax.scatter(x, y, marker=marker, s=40,  # s is the size of the marker
                       facecolors=ink if fill_style == 'full' else 'none',  # Set face color based on team
                       edgecolors=ink,  # Set edge color to be always ink
                       linewidths=2)  # Adjust linewidths for visibility

    ax.set_xlabel(f"simulation {j+1}", color=ink)
    ax.set_facecolor(bg)
    ticks = np.arange(2, 31, tick_interval)  # Assuming your grid goes from 0 to 32
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.tick_params(colors=ink, direction='in', length=6, width=1, which='both',
                   top=True, bottom=True, left=True, right=True, labelleft=False, labelbottom=False)
    ax.spines['top'].set_color(ink)
    ax.spines['bottom'].set_color(ink)
    ax.spines['left'].set_color(ink)
    ax.spines['right'].set_color(ink)
    ax.set_aspect('equal')
    ax.set_xlim(-2, 34)
    ax.set_ylim(-2, 34)
