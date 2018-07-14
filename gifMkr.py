from sort import sorted_alphanumeric
import os
import imageio

def gifMkr(impath = None, gifpath = None, giftitle=None):

	if(impath==None):
	    impath = os.getcwd()+'/images/'
	
	if(gifpath==None):
	    gifpath = os.getcwd()+'/gif/'

	if(giftitle==None):
	    giftitle='test.gif'

	images = []
	for file_name in sorted_alphanumeric(os.listdir(impath)):
		if file_name.endswith('.png'):
		       	file_path = os.path.join(impath, file_name)
		    	images.append(imageio.imread(file_path))

	kargs = {'duration': 0.1}
	imageio.mimsave(gifpath+giftitle, images, **kargs)
