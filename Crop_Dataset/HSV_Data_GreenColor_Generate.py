import cv2
import os
import numpy as np
from tqdm import tqdm

input_dir = "Data/images"

output_dir_hsv = "HSV_data/images"

output_dir_mask = "HSV_data/masks"

if not os.path.exists(output_dir_hsv):
    os.makedirs(output_dir_hsv)

if not os.path.exists(output_dir_mask):
    os.makedirs(output_dir_mask)

for filename in tqdm(os.listdir(input_dir)):
    img = cv2.imread(os.path.join(input_dir, filename))

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_green = np.array([30, 20, 20])
    upper_green = np.array([75, 255, 255])

    mask = cv2.inRange(hsv, lower_green, upper_green)
    result = cv2.bitwise_and(img, img, mask=mask)
    cv2.imwrite(os.path.join(output_dir_hsv, "HSV_G" + filename.rsplit('.',1)[0] + '.png'), result)

    mask_binary = np.zeros_like(mask)
    mask_binary[mask == 255] = 3
    cv2.imwrite(os.path.join(output_dir_mask, "MSK_HSV_G" + filename.rsplit('.',1)[0] + '.png'), mask_binary)