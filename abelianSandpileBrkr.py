import time
import os
import numpy as np
import matplotlib.pyplot as plt
import sys

def dropSandBrkr(s = None, top = None, fp = None, pos = None, breaks = None):

    #  default size of our field
    if(s == None):
        s = (240, 240)

    # maximum number of grains should be natural number multiples of 4
    if(top==None):
        top = 4

    # first pile
    if(fp==None):
        fp = 10000
    # location of first pile
    if(pos==None):
        pos = (120,120)

    # define break for saving plots
    if(breaks==None):
        sys.exit("breaks must be defined in dropSand")

    # sand field
    field = np.zeros((s[0],s[1]))
    field[pos[0],pos[1]] += fp

    i = 0
    t0 = time.time()

    while np.max(field) >= top:

	# find the largest piles
        high = field >= top

        # decrease high piles by top
        field[high] -= top

	right = (np.where(high)[0]+1, np.where(high)[1])
	left = (np.where(high)[0]-1, np.where(high)[1])
	up = (np.where(high)[0], np.where(high)[1]+1)
	down = (np.where(high)[0], np.where(high)[1]-1)

	field[right] += top/4
	field[left] += top/4
	field[up] += top/4
	field[down] += top/4

        if(i > 20 and i % breaks == 0):
		maxi = np.max(np.where(field == 1)[0])
		fig = plt.imshow(field, vmin = 0, vmax= 3)
		plt.xlim(235-maxi,maxi+5)
		plt.ylim(235-maxi,maxi+5)
		plt.axis('off')
		fig.axes.get_xaxis().set_visible(False)
		fig.axes.get_yaxis().set_visible(False)
		plt.savefig(os.getcwd()+"/images/"+str(i)+"_sandpile_"+str(fp)+".png", frameon=False, bbox_inches='tight')

        i += 1

    t1 = time.time()
    print("%d iterations in %.2f seconds" % (i, t1-t0))
    return (field,fp)
