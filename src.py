from abelianSandpile import dropSand
import numpy as np
import matplotlib.pyplot as plt
import os
import imageio

# implementing dropSand to generate .png files

fps = (20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000)

for i in range(len(fps)):

	test = dropSand(fp = fps[i])
	fp = test[1]
	img = test[0]
	maxi = np.max(np.where(img == 1)[0])

	fig = plt.imshow(img, vmin = 0, vmax= 3)
	plt.xlim(235-maxi,maxi+5)
	plt.ylim(235-maxi,maxi+5)
	plt.axis('off')
	fig.axes.get_xaxis().set_visible(False)
	fig.axes.get_yaxis().set_visible(False)

	plt.savefig(os.getcwd()+"/images/"+str(i)+"_sandpile_"+str(fp)+".png", frameon=False, bbox_inches='tight')
