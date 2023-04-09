# Code for visualizing MASK images - just for recheck
# All Mask images will be taken from masks folder and save visualization into visualize folder.
# masks and visualization folder must be in the same directory with this code

import os
from PIL import Image


image_dir = 'visualize'
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

folder_path = 'masks'
file_save_path = 'visualize'


for file_name in os.listdir(folder_path):

    if file_name.endswith(".bmp") or file_name.endswith(".png") or file_name.endswith(".jpeg") or file_name.endswith(".jpg"):
        img = Image.open(os.path.join(folder_path, file_name))
        
        img = img.point(lambda x: 255 if x > 0 else 0)
        
        img.save(os.path.join(file_save_path, file_name))