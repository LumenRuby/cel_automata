import numpy as np
import cellpylib as cpl
import matplotlib.pyplot as plt
import matplotlib.animation as anima


automaton = cpl.init_random2d(60, 60)

automaton = cpl.evolve2d(automaton, timesteps = 250, neighbourhood = 'Moore', apply_rule = cpl.game_of_life_rule, memoize = 'recursive')

fig, ax = plt.subplots()
ax.set_xlim((0,60))
ax.set_ylim((0,60))

img = ax.imshow(automaton[0], interpolation = 'nearest', cmap = 'Greys')

def init():
    img.set_data(automaton[0])
    return (img,)

def animate(i):
    img.set_data(automaton[i])
    return (img,)

ani = anima.FuncAnimation(fig, animate, init_func = init, frames = 250, interval = 30, blit = True, repeat = False)
plt.show()