# worlds.py
#   plots simulated worlds (SORTSOL and C2SIM)
# by: Noah Syrkis

# imports
import matplotlib.pyplot as plt
import numpy as np
import imageio
import darkdetect

def worlds_fn(seqs):
    bg = 'black' if darkdetect.isDark() else 'white'
    ink = 'black' if bg == 'white' else 'white'
    grid_size = (4, 4)  # For a 4x4 grid
    figsize = (16, 16)  # Size of the figure, adjust as needed

    # Prepare a list to hold all frames (as NumPy arrays)
    frames = []
    n = seqs.state.unit_positions.shape[0]
    for i in range(n):
        fig, axes = plt.subplots(*grid_size, figsize=figsize, facecolor=bg, dpi=100)  # Set background to black
        for j, ax in enumerate(axes.flatten()):
            pos = seqs.state.unit_positions[i, j, :, :]
            ax.scatter(pos[:, 0], pos[:, 1], color=ink)  # Set dots to white
            ax.set_title(f"Simulation {j+1}, step {str(i).zfill(2)}", color=ink)  # Set title text to white
            ax.set_facecolor(bg) 
            ax.set_xticks([])
            ax.set_yticks([])
            ax.spines['top'].set_color(ink)
            ax.spines['bottom'].set_color(ink)
            ax.spines['left'].set_color(ink)
            ax.spines['right'].set_color(ink)
            ax.set_aspect('equal')
            # ax.axis('off')
            ax.set_xlim(0, 32)  # Set X-axis limits
            ax.set_ylim(0, 32)  # Set Y-axis limits
        plt.tight_layout()
        fig.canvas.draw()
        data = np.frombuffer(fig.canvas.buffer_rgba(), dtype=np.uint8)
        data = data.reshape(fig.canvas.get_width_height()[::-1] + (4,))[:, :, :3]
        frames.append(data)
        plt.close(fig)

    imageio.mimsave('docs/worlds.gif', frames, duration=n/24, loop=0)