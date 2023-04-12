# Code for visualizing MASK images - just for recheck
# All Mask images will be taken from masks folder and save visualization into visualize folder.
# masks and visualization folder must be in the same directory with this code

import os
from PIL import Image
from tqdm import tqdm


image_dir = 'Data/visualize'
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

folder_path = 'Data/masks'

for file_name in tqdm(os.listdir(folder_path)):

    if file_name.endswith(".png") or file_name.endswith(".jpg"):
        img = Image.open(os.path.join(folder_path, file_name))
        
        img = img.point(lambda x: 255 if x > 0 else 0)
        
        img.save(os.path.join(image_dir,"Visualize_"+ file_name.rsplit('.',1)[0] + '.png'))