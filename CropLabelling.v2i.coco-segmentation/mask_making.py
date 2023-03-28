# Code for generate MASK images
# All images and COCO-JSON file must be in the same directory with this python file
# Then all images will be move to images folder and MSK_images will move to masks folder


import json
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import cv2
import os
import shutil
import numpy as np

# Load the JSON file
with open('_annotations.coco.json') as f:
    data = json.load(f)

mask_dir = 'masks'
if not os.path.exists(mask_dir):
    os.makedirs(mask_dir)
image_dir = 'images'
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

# Loop through each image in the JSON file
for image_data in data['images']:
    # Get the annotations for the current image
    image_annotations = [annotation for annotation in data['annotations'] if annotation['image_id'] == image_data['id']]

    # Create a blank image with the same size as the original image
    binary_image = np.zeros((image_data['height'], image_data['width']))

    # Fill the polygons with white pixels (value of 1)
    for annotation in image_annotations:
        segmentation = annotation['segmentation'][0]
        pts = np.array(segmentation, np.int32)
        pts = pts.reshape((-1, 2))
        cv2.fillPoly(binary_image, [pts], color=1)

    # Set the x and y limits of the axes
    #plt.imshow(plt.imread(image_data['file_name']))
    #plt.show()
    cv2.imwrite(os.path.join('masks', f'MSK_{image_data["file_name"]}'), binary_image)
    #plt.imshow(plt.imread(image_data['file_name']))
    # plt.savefig(os.path.join('masks', f'MSK_{image_data["file_name"]}'))

for filename in os.listdir('.'):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        shutil.move(filename, os.path.join('images', filename))
