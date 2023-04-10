import os
from PIL import Image
import random
import numpy as np
from tqdm import tqdm

if not os.path.exists('RGB_zero'):
    os.makedirs('RGB_zero')

mask_dir = 'masks'
img_dir = 'images'

file_save_path = 'RGB_zero'
for mask_file in tqdm(os.listdir(mask_dir)):
    if mask_file.startswith('MSK_'):
        img_file = mask_file[4:].replace(".png", ".jpg")
        img_path = os.path.join(img_dir, img_file)
        mask_path = os.path.join(mask_dir, mask_file)

        mask_img = Image.open(mask_path)
        img = Image.open(img_path)

        width, height = img.size
        for x in range(width):
            for y in range(height):
                if mask_img.getpixel((x, y)) == 1:
                    img.putpixel((x, y), (0, 0, 0))

        new_img_path = os.path.join(file_save_path, 'RGB_' + img_file.rsplit('.',1)[0] + '.png')
        img.save(new_img_path)