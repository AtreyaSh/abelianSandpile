from abelianSandpileBrkr import dropSandBrkr
import os
import imageio
import re

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(data, key=alphanum_key)

# Utilizing our images to create our gif

dropSandBrkr(breaks = 100)

png_dir = os.getcwd()+'/images/'
images = []
for file_name in sorted_alphanumeric(os.listdir(png_dir)):
	if file_name.endswith('.png'):
		file_path = os.path.join(png_dir, file_name)
		images.append(imageio.imread(file_path))

kargs = { 'duration': 0.1}
imageio.mimsave(os.getcwd()+'/gif/sandyMovie.gif', images, **kargs)
