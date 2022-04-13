import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def transmission(truth_rays):
    success = np.sum(np.all(truth_rays, axis=1))
    total = float(truth_rays.shape[0])
    return (success/total)


def plot_rays(output_rays, elements=True, device=None,
              alpha=0.1, coor=0, ray_color='#684762',
              hit_color='#800806', element_color='k', hit_alpha=1.0):
    
    fig, ax = plt.subplots(1)
    if elements:
        plot_elements(fig, ax, device, element_color=element_color)
    for ele in output_rays:
        if device:
            ax.plot(device.z, ele[:, coor], alpha=alpha, color=ray_color, marker='None', lw=0.5)
        else:
            ax.plot(ele[:, coor], alpha=alpha, color=ray_color, marker='None', lw=0.5)
            
    plt.xlabel('Beamline Distance (m)', fontsize=20)
    if coor == 0:
        plt.ylabel('x (m)', fontsize=20)
    elif coor == 2:
        plt.ylabel('y (m)', fontsize=20)
    else:
        plt.ylabel('Some Coordinate...', fontsize=20)
    plt.ylim(-0.25, 0.25)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.tight_layout()

def plot_elements(fig, ax, device, element_color='k'):
    z = 0.0
    for i, ele in enumerate(device.elements):
        z0 = z
        z += ele.z_lim
        #ax.text(z0, loc, ele.name, fontsize=10.0)
        rect = Rectangle((z0, -ele.x_lim), ele.z_lim, 2*ele.x_lim, linewidth=1,edgecolor=element_color, facecolor='none')
        ax.set_zorder = -100
        ax.add_patch(rect)
