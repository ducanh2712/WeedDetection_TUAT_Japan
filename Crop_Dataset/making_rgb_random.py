# Code for replacing RGB = (0,0,0) values with random Gauss values with mean generated from mean of 3 channel R,G,B

import os
from PIL import Image
import random
import numpy as np
from tqdm import tqdm

input_dir = "RGB_zero"

output_dir = "RGB_random"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for filename in tqdm(os.listdir(input_dir)):
    if filename.startswith("RGB_") and ( filename.endswith(".jpg") or filename.endswith(".png")) :
        img_path = os.path.join(input_dir, filename)
        img = Image.open(img_path)
        width, height = img.size
        means = np.mean(img, axis=(0,1))
        for x in range(width):
            for y in range(height):
                r, g, b = img.getpixel((x, y))
                if r <= 20 and g <= 20 and b <= 20:
                    new_r = random.gauss(means[0], 64)
                    new_g = random.gauss(means[1], 64)
                    new_b = random.gauss(means[2], 64)
                    img.putpixel((x, y), (int(new_r), int(new_g), int(new_b)))

        new_filename = "Gauss_" + filename.replace("RGB_", "")
        new_img_path = os.path.join(output_dir, new_filename.rsplit('.',1)[0] + '.png')
        img.save(new_img_path)