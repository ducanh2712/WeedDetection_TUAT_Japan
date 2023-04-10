"""
Making fixed and artificial images
"""
import cv2
import os
import numpy as np
import random
from tqdm import tqdm

def load_images(directory:str)->list:
    """
    input: Path to directory of images
    output: list of image(np.ndarray)
    """
    image_list = []
    sorted_filenames = sorted(os.listdir(directory)) # Sort alphabetically
    for filename in sorted_filenames:
        img = cv2.imread(os.path.join(directory, filename))
        image_list.append(img)
    return image_list

def split_img(original:np.ndarray, crop_mask:np.ndarray):
    """
    input: original(raw image), crop_mask(binary image with 3 channels)
    output: (crop_only(RGB image of crop without background), no_crop(RGB image of background without crop))
    """
    # image_crop: maskのピクセルが1の部分だけを残す
    crop_only = np.where(crop_mask == 1, original, 0)

    # image_back: maskのピクセルが0の部分だけを残す
    no_crop = np.where(crop_mask == 0, original, 0)

    return crop_only, no_crop


def generate_slided(no_crop:np.ndarray, slide_max=0.3)->np.ndarray:
    """
    Function for making fixed image
    input
    no_crop(RGB image of background without crop)
    slide_max: max ratio of sliding image
    output: Images moved horizontally and vertically in parallel
    """

    width = no_crop.shape[1]
    height = no_crop.shape[0]

    translated_img = np.zeros_like(no_crop)

    signx = random.choice([-1, 1])
    signy = random.choice([-1, 1])

    slidex = signx*(int(width*slide_max*0.7) + np.random.randint(0, int(width*slide_max*0.3)))
    slidey = signy*(int(height*slide_max*0.7) + np.random.randint(0, int(width*slide_max*0.3)))

    if slidex < 0:
        start_x = -slidex
        end_x = width
        target_start_x = 0
        target_end_x = width + slidex
    else:
        start_x = 0
        end_x = width - slidex
        target_start_x = slidex
        target_end_x = width

    if slidey < 0:
        start_y = -slidey
        end_y = height
        target_start_y = 0
        target_end_y = height + slidey
    else:
        start_y = 0
        end_y = height - slidey
        target_start_y = slidey
        target_end_y = height

    translated_img[target_start_y:target_end_y, target_start_x:target_end_x] =\
        no_crop[start_y:end_y, start_x:end_x]
    
    return translated_img

def fill_black_pixel_with_copy(no_crop:np.ndarray, loop=100)->np.ndarray:
    """
    Function for filling black pixel with copied pixels in same image
    input
    no_crop(RGB image of background without crop)
    loop(the number of addition no_crop and random slided image)

    output
    fixed(image that have filled black pixels)
    """
    fixed = np.copy(no_crop)

    for i in range(0, loop):
        fixed_mask = np.all(fixed == (0, 0, 0), axis=-1).astype(int)
        fixed_mask = np.repeat(fixed_mask[:, :, np.newaxis], 3, axis=2)

        slided_img = generate_slided(no_crop)
        fill_img = np.where(fixed_mask == 1, slided_img, 0)
        fixed += fill_img

        if i % 10 == 0:
            zero_mask = np.all(fixed == (0, 0, 0), axis=-1).astype(int)
            black_count = np.count_nonzero(zero_mask == 1)

            if black_count == 0:
                return fixed

    return fixed

def make_artificial_image_and_cropmask(crop_only:np.ndarray, fixed:np.ndarray)->tuple:
    """
    input:
    crop_only(RGB image of crop without background)
    fixed(image that have filled black pixels)

    output: 
    (artificial_image(RGB image), crop_mask)
    """
    crop_mask = np.all(crop_only != (0, 0, 0), axis=-1).astype(int)
    crop_mask = np.repeat(crop_mask[:, :, np.newaxis], 3, axis=2)
    fixed_with_black = np.where(crop_mask == 0, fixed, 0)
    artificial_image = fixed_with_black + crop_only
    return artificial_image, crop_mask

if __name__ == '__main__':
    MASK_DIR = 'Data/masks'
    IMG_DIR = 'Data/images'

    # 画像が格納されているディレクトリのパスを指定してください
    original_list = load_images(IMG_DIR)
    crop_mask_list = load_images(MASK_DIR)

    no_crop_list = []
    crop_only_list = []
    for original, crop_mask in tqdm(zip(original_list, crop_mask_list)):
        crop_only, no_crop = split_img(original, crop_mask)
        crop_only_list.append(crop_only)
        no_crop_list.append(no_crop)
    original_list.clear()
    crop_mask_list.clear()

    fixed_list = [fill_black_pixel_with_copy(no_crop) for no_crop in no_crop_list]
    no_crop_list.clear()

    artificial_image_list = []
    artificial_mask_list = []
    for fixed in tqdm(fixed_list):
        for crop_only in crop_only_list:
            artificial_image, artificial_mask = make_artificial_image_and_cropmask(crop_only, fixed)
            artificial_image_list.append(artificial_image)
            artificial_mask_list.append(artificial_mask)
    
    cv2.imshow("Artificial image example",artificial_image_list[-1])
    cv2.waitKey(0)
