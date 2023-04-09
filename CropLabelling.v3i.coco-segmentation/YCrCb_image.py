import cv2
import os
import numpy as np

input_dir = "images"

output_dir_ycrcb = "green_YCrCb"

output_dir_mask = "green_MSK_YCrCb"

if not os.path.exists(output_dir_ycrcb):
    os.makedirs(output_dir_ycrcb)

if not os.path.exists(output_dir_mask):
    os.makedirs(output_dir_mask)

for filename in os.listdir(input_dir):
    img = cv2.imread(os.path.join(input_dir, filename))

    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)

    lower_green = np.array([0, 90, 0])
    upper_green = np.array([255, 150, 255])

    mask = cv2.inRange(ycrcb, lower_green, upper_green)
    result = cv2.bitwise_and(img, img, mask=mask)
    cv2.imwrite(os.path.join(output_dir_ycrcb, "green_YCrCb_" + filename), result)

    mask_binary = np.zeros_like(mask)
    mask_binary[mask == 255] = 3
    cv2.imwrite(os.path.join(output_dir_mask, "green_MSK_YCrCb" + filename), mask_binary)
