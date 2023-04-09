import cv2
import os
import numpy as np

output_dir = "FIXED"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

image_dat = cv2.imread('background.JPG')

mean_rgb_dat = cv2.mean(image_dat)[:3]

folder_path = 'RGB_zero'
for filename in os.listdir(folder_path):
    if filename.startswith('RGB_'):
        image_rgb = cv2.imread(os.path.join(folder_path, filename))
        image_rgb[np.where((image_rgb < 20).all(axis=2))] = mean_rgb_dat
        cv2.imwrite(os.path.join('FIXED', 'FIXED_' + filename), image_rgb)
