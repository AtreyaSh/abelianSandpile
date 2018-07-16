from abelianSandpile import dropSand
import numpy as np
import matplotlib.pyplot as plt
import os
import imageio
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

# implementing dropSand to generate .png files

test = dropSand(fp=10000)

fig = plt.figure(figsize=(120, 120))
ax1 = fig.add_subplot(121, projection='3d')

x = np.where(test[0])[0]
y = np.where(test[0])[1]
top = test[0][x,y]

bottom = np.zeros_like(top)
width = 0.8
depth = 0.8
cmap = cm.get_cmap('jet')
max_ht = np.max(top)
min_ht = np.min(top)

rgba = [cmap((k-min_ht)/max_ht) for k in top]

ax1.bar3d(x, y, bottom, width, depth, top, shade=True, color=rgba)

plt.show()

#plt.savefig(os.getcwd()+"/images/"+str(i)+"_sandpile_"+str(fp)+".png", frameon=False, bbox_inches='tight')
